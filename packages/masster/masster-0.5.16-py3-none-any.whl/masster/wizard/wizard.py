"""
Wizard module for automated processing of mass spectrometry studies.

This module provides the Wizard class for fully automated processing of MS data
from raw files to final study results, including batch conversion, assembly,
alignment, merging, plotting, and export.

Key Features:
- Automated discovery and batch conversion of raw data files
- Intelligent resume capability for interrupted processes
- Parallel processing optimization for large datasets
- Adaptive study format based on study size
- Comprehensive logging and progress tracking
- Optimized memory management for large studies

Classes:
- Wizard: Main class for automated study processing
- wizard_def: Default parameters configuration class

Example Usage:
```python
from masster import Wizard, wizard_def

# Create wizard with default parameters
wizard = Wizard(
    source="./raw_data",
    folder="./processed_study",
    polarity="positive",
    num_cores=4
)

```
"""

from __future__ import annotations

import os
import sys
import time
import importlib
import glob
import multiprocessing
from pathlib import Path
from typing import Optional, Any, Dict, List
from dataclasses import dataclass, field
import concurrent.futures
from datetime import datetime

# Import masster modules - use delayed import to avoid circular dependencies
from masster.logger import MassterLogger
from masster.study.defaults.study_def import study_defaults
from masster.study.defaults.align_def import align_defaults
from masster.study.defaults.merge_def import merge_defaults
from masster._version import __version__ as version


@dataclass
class wizard_def:
    """
    Default parameters for the Wizard automated processing system.
    
    This class provides comprehensive configuration for all stages of automated
    mass spectrometry data processing from raw files to final results.
    
    Attributes:
        # Core Configuration
        source (str): Path to directory containing raw data files
        folder (str): Output directory for processed study
        polarity (str): Ion polarity mode ("positive" or "negative")
        num_cores (int): Number of CPU cores to use for parallel processing
        
        # File Discovery
        file_extensions (List[str]): File extensions to search for
        search_subfolders (bool): Whether to search subdirectories
        skip_patterns (List[str]): Filename patterns to skip
        
        # Processing Parameters
        adducts (List[str]): Adduct specifications for given polarity
        batch_size (int): Number of files to process per batch
        memory_limit_gb (float): Memory limit for processing (GB)
        
        # Resume & Recovery
        resume_enabled (bool): Enable automatic resume capability
        force_reprocess (bool): Force reprocessing of existing files
        backup_enabled (bool): Create backups of intermediate results
        
        # Output & Export
        generate_plots (bool): Generate visualization plots
        export_formats (List[str]): Output formats to generate
        compress_output (bool): Compress final study file
        
        # Logging
        log_level (str): Logging detail level
        log_to_file (bool): Save logs to file
        progress_interval (int): Progress update interval (seconds)
    """
    
    # === Core Configuration ===
    source: str = ""
    folder: str = ""  
    polarity: str = "positive"
    num_cores: int = 4
    
    # === File Discovery ===
    file_extensions: List[str] = field(default_factory=lambda: [".wiff", ".raw", ".mzML"])
    search_subfolders: bool = True
    skip_patterns: List[str] = field(default_factory=lambda: ["blank", "test"])
    
    # === Processing Parameters ===
    adducts: List[str] = field(default_factory=list)  # Will be set based on polarity
    batch_size: int = 8
    memory_limit_gb: float = 16.0
    max_file_size_gb: float = 4.0
    
    # === Resume & Recovery ===
    resume_enabled: bool = True
    force_reprocess: bool = False
    backup_enabled: bool = True
    checkpoint_interval: int = 10  # Save progress every N files
    
    # === Study Assembly ===
    min_samples_for_merge: int = 2
    rt_tolerance: float = 1.5
    mz_max_diff: float = 0.01
    alignment_algorithm: str = "kd"
    merge_method: str = "qt"
    
    # === Feature Detection ===
    chrom_fwhm: float = 0.5
    noise: float = 50.0
    chrom_peak_snr: float = 5.0
    tol_ppm: float = 10.0
    detector_type: str = "unknown"  # Detected detector type ("orbitrap", "quadrupole", "unknown")
    
    # === Output & Export ===
    generate_plots: bool = True
    generate_interactive: bool = True
    export_formats: List[str] = field(default_factory=lambda: ["csv", "mgf", "xlsx"])
    compress_output: bool = True
    adaptive_compression: bool = True  # Adapt based on study size
    
    # === Logging ===
    log_level: str = "INFO"
    log_to_file: bool = True
    progress_interval: int = 30  # seconds
    verbose_progress: bool = True
    
    # === Advanced Options ===
    use_process_pool: bool = True  # vs ThreadPoolExecutor
    optimize_memory: bool = True
    cleanup_temp_files: bool = True
    validate_outputs: bool = True
        
    _param_metadata: dict[str, dict[str, Any]] = field(
        default_factory=lambda: {
            "source": {
                "dtype": str,
                "description": "Path to directory containing raw data files",
                "required": True,
            },
            "folder": {
                "dtype": str, 
                "description": "Output directory for processed study",
                "required": True,
            },
            "polarity": {
                "dtype": str,
                "description": "Ion polarity mode",
                "default": "positive",
                "allowed_values": ["positive", "negative", "pos", "neg"],
            },
            "num_cores": {
                "dtype": int,
                "description": "Number of CPU cores to use",
                "default": 4,
                "min_value": 1,
                "max_value": multiprocessing.cpu_count(),
            },
            "batch_size": {
                "dtype": int,
                "description": "Number of files to process per batch",
                "default": 8,
                "min_value": 1,
                "max_value": 32,
            },
            "memory_limit_gb": {
                "dtype": float,
                "description": "Memory limit for processing (GB)",
                "default": 16.0,
                "min_value": 1.0,
                "max_value": 128.0,
            },
        },
        repr=False,
    )
    
    def __post_init__(self):
        """Set polarity-specific defaults after initialization."""
        # Set default adducts based on polarity if not provided
        if not self.adducts:
            if self.polarity.lower() in ["positive", "pos"]:
                self.adducts = ["H:+:0.8", "Na:+:0.1", "NH4:+:0.1"]
            elif self.polarity.lower() in ["negative", "neg"]: 
                self.adducts = ["H-1:-:1.0", "CH2O2:0:0.5"]
            else:
                # Default to positive
                self.adducts = ["H:+:0.8", "Na:+:0.1", "NH4:+:0.1"]
        
        # Validate num_cores
        max_cores = multiprocessing.cpu_count()
        if self.num_cores <= 0:
            self.num_cores = max_cores
        elif self.num_cores > max_cores:
            self.num_cores = max_cores
            
        # Ensure paths are absolute
        if self.source:
            self.source = os.path.abspath(self.source)
        if self.folder:
            self.folder = os.path.abspath(self.folder)


class Wizard:
    """
    Simplified Wizard for automated mass spectrometry data processing.
    
    The Wizard provides a clean interface for creating and executing analysis scripts
    that process raw MS data through the complete pipeline: file discovery, feature
    detection, sample processing, study assembly, alignment, merging, and export.
    
    This simplified version focuses on two core functions:
    - create_scripts(): Generate standalone analysis scripts
    - execute(): Create and run analysis scripts
    """
    
    def __init__(
        self,
        source: str = "",
        folder: str = "",
        polarity: str = "positive",
        adducts: Optional[List[str]] = None,
        num_cores: int = 6,
        **kwargs
    ):
        """
        Initialize the Wizard with analysis parameters.
        
        Parameters:
            source: Directory containing raw data files
            folder: Output directory for processed study
            polarity: Ion polarity mode ("positive" or "negative")
            adducts: List of adduct specifications (auto-set if None)
            num_cores: Number of CPU cores (0 = auto-detect 75% of available)
            **kwargs: Additional parameters (see wizard_def for full list)
        """
        
        # Auto-detect optimal number of cores if not specified
        if num_cores <= 0:
            num_cores = max(1, int(multiprocessing.cpu_count() * 0.75))
            
        # Create parameters instance
        if "params" in kwargs and isinstance(kwargs["params"], wizard_def):
            self.params = kwargs.pop("params")
        else:
            # Create default parameters
            self.params = wizard_def(
                source=source,
                folder=folder,
                polarity=polarity,
                num_cores=num_cores
            )
            
            # Set adducts if provided
            if adducts is not None:
                self.params.adducts = adducts
            
            # Update with any additional parameters
            for key, value in kwargs.items():
                if hasattr(self.params, key):
                    setattr(self.params, key, value)
        
        # Validate required parameters
        if not self.params.source:
            raise ValueError("source is required")
        if not self.params.folder:
            raise ValueError("folder is required")
        
        # Create and validate paths
        self.source_path = Path(self.params.source)
        self.folder_path = Path(self.params.folder) 
        self.folder_path.mkdir(parents=True, exist_ok=True)
        
        # Auto-infer polarity from the first file if not explicitly set by user
        if polarity == "positive" and "polarity" not in kwargs:
            inferred_polarity = self._infer_polarity_from_first_file()
            if inferred_polarity:
                self.params.polarity = inferred_polarity
                # Update adducts based on inferred polarity  
                self.params.__post_init__()

    def _infer_polarity_from_first_file(self) -> str:
        """
        Infer polarity from the first available raw data file.
        
        Returns:
            Inferred polarity string ("positive" or "negative") or None if detection fails
        """
        try:
            # Find first file
            for extension in ['.wiff', '.raw', '.mzML']:
                pattern = f"**/*{extension}" if True else f"*{extension}"  # search_subfolders=True
                files = list(self.source_path.rglob(pattern))
                if files:
                    first_file = files[0]
                    break
            else:
                return 'positive'

            # Only implement for .wiff files initially (most common format)
            if first_file.suffix.lower() == '.wiff':
                from masster.sample.load import _wiff_to_dict
                
                # Extract metadata from first file
                metadata_df = _wiff_to_dict(str(first_file))
                
                if not metadata_df.empty and 'polarity' in metadata_df.columns:
                    # Get polarity from first experiment  
                    first_polarity = metadata_df['polarity'].iloc[0]
                    
                    # Convert numeric polarity codes to string
                    if first_polarity == 1 or str(first_polarity).lower() in ['positive', 'pos', '+']:
                        return "positive"
                    elif first_polarity == -1 or str(first_polarity).lower() in ['negative', 'neg', '-']:
                        return "negative"
                    
        except Exception:
            # Silently fall back to default if inference fails
            pass
            
        return 'positive'

    @property
    def polarity(self) -> str:
        """Get the ion polarity mode."""
        return self.params.polarity

    @property
    def adducts(self) -> List[str]:
        """Get the adduct specifications."""
        return self.params.adducts

    def create_scripts(self) -> Dict[str, Any]:
        """
        Generate analysis scripts based on source file analysis.
        
        This method:
        1. Analyzes the source files to extract metadata
        2. Creates 1_masster_workflow.py with sample processing logic
        3. Creates 2_interactive_analysis.py marimo notebook for study exploration
        4. Returns instructions for next steps
        
        Returns:
            Dictionary containing:
            - status: "success" or "error"
            - message: Status message
            - instructions: List of next steps
            - files_created: List of created file paths
            - source_info: Metadata about source files
        """
        try:
            # Step 1: Analyze source files to extract metadata
            source_info = self._analyze_source_files()
            
            # Update wizard parameters based on detected metadata
            if source_info.get('polarity') and source_info['polarity'] != 'positive':
                self.params.polarity = source_info['polarity']
            
            files_created = []
            
            # Step 2: Create 1_masster_workflow.py
            workflow_script_path = self.folder_path / "1_masster_workflow.py"
            workflow_content = self._generate_workflow_script_content(source_info)
            
            with open(workflow_script_path, 'w', encoding='utf-8') as f:
                f.write(workflow_content)
            files_created.append(str(workflow_script_path))
            
            # Step 3: Create 2_interactive_analysis.py marimo notebook
            notebook_path = self.folder_path / "2_interactive_analysis.py"
            notebook_content = self._generate_interactive_notebook_content(source_info)
            
            with open(notebook_path, 'w', encoding='utf-8') as f:
                f.write(notebook_content)
            files_created.append(str(notebook_path))
            
            # Step 4: Generate instructions
            instructions = self._generate_instructions(source_info, files_created)
            
            return {
                "status": "success",
                "message": f"Successfully created {len(files_created)} script files",
                "instructions": instructions,
                "files_created": files_created,
                "source_info": source_info
            }
            
        except Exception as e:
            return {
                "status": "error", 
                "message": f"Failed to create scripts: {e}",
                "instructions": [],
                "files_created": [],
                "source_info": {}
            }

    def _analyze_source_files(self) -> Dict[str, Any]:
        """Analyze source files to extract metadata."""
        result = {
            "number_of_files": 0,
            "file_types": [],
            "polarity": "positive", 
            "length_minutes": 0.0,
            "first_file": None
        }
        
        try:
            # Find raw data files
            extensions = [".wiff", ".raw", ".mzML"]
            raw_files = []
            
            for ext in extensions:
                pattern = f"**/*{ext}"
                files = list(self.source_path.rglob(pattern))
                if files:
                    raw_files.extend(files)
                    if ext not in result["file_types"]:
                        result["file_types"].append(ext)
            
            result["number_of_files"] = len(raw_files)
            
            if raw_files:
                result["first_file"] = str(raw_files[0])
                # Simple heuristic: assume 30 minutes per file if we can't determine
                result["length_minutes"] = 30.0
                
        except Exception as e:
            print(f"Warning: Could not analyze source files: {e}")
            
        return result

    def _generate_workflow_script_content(self, source_info: Dict[str, Any]) -> str:
        """Generate the content for 1_masster_workflow.py script."""
        
        script_lines = [
            '#!/usr/bin/env python3',
            '"""',
            'Automated Mass Spectrometry Data Analysis Pipeline',
            'Generated by masster wizard',
            '"""',
            '',
            'import sys',
            'import time',
            'from pathlib import Path',
            '',
            '# Import masster modules',
            'from masster.study import Study',
            'from masster import __version__',
            '',
            '# Analysis parameters',
            'PARAMS = {',
            '    # === Core Configuration ===',
            f'    "source": {str(self.source_path)!r},  # Directory containing raw data files',
            f'    "folder": {str(self.folder_path)!r},  # Output directory for processed study',
            f'    "polarity": {self.params.polarity!r},  # Ion polarity mode ("positive" or "negative")',
            f'    "num_cores": {self.params.num_cores},  # Number of CPU cores for parallel processing',
            '',
            '    # === File Discovery ===',
            f'    "file_extensions": {self.params.file_extensions!r},  # File extensions to search for',
            f'    "search_subfolders": {self.params.search_subfolders},  # Whether to search subdirectories recursively',
            f'    "skip_patterns": {self.params.skip_patterns!r},  # Filename patterns to skip',
            '',
            '    # === Processing Parameters ===',
            f'    "adducts": {self.params.adducts!r},  # Adduct specifications for feature detection and annotation',
            f'    "noise": {self.params.noise},  # Noise threshold for feature detection',
            f'    "chrom_fwhm": {self.params.chrom_fwhm},  # Chromatographic peak full width at half maximum (seconds)',
            f'    "chrom_peak_snr": {self.params.chrom_peak_snr},  # Minimum signal-to-noise ratio for chromatographic peaks',
            '',
            '    # === Alignment & Merging ===',
            f'    "rt_tol": {self.params.rt_tolerance},  # Retention time tolerance for alignment (seconds)',
            f'    "mz_tol": {self.params.mz_max_diff},  # Mass-to-charge ratio tolerance for alignment (Da)',
            f'    "alignment_method": {self.params.alignment_algorithm!r},  # Algorithm for sample alignment',
            f'    "min_samples_per_feature": {self.params.min_samples_for_merge},  # Minimum samples required per consensus feature',
            f'    "merge_method": {self.params.merge_method!r},  # Method for merging consensus features',
            '',
            '    # === Sample Processing (used in add_samples_from_folder) ===',
            f'    "batch_size": {self.params.batch_size},  # Number of files to process per batch',
            f'    "memory_limit_gb": {self.params.memory_limit_gb},  # Memory limit for processing (GB)',
            '',
            '    # === Script Options ===',
            f'    "resume_enabled": {self.params.resume_enabled},  # Enable automatic resume capability',
            f'    "force_reprocess": {self.params.force_reprocess},  # Force reprocessing of existing files',
            f'    "cleanup_temp_files": {self.params.cleanup_temp_files},  # Clean up temporary files after processing',
            '}',
            '',
            '',
            'def discover_raw_files(source_folder, file_extensions, search_subfolders=True):',
            '    """Discover raw data files in the source folder."""',
            '    source_path = Path(source_folder)',
            '    raw_files = []',
            '    ',
            '    for ext in file_extensions:',
            '        if search_subfolders:',
            '            pattern = f"**/*{ext}"',
            '            files = list(source_path.rglob(pattern))',
            '        else:',
            '            pattern = f"*{ext}"',
            '            files = list(source_path.glob(pattern))',
            '        raw_files.extend(files)',
            '    ',
            '    return raw_files',
            '',
            '',
            'def process_single_file(args):',
            '    """Process a single raw file to sample5 format - module level for multiprocessing."""',
            '    raw_file, output_folder = args',
            '    from masster.sample import Sample',
            '    ',
            '    try:',
            '        # Create sample5 filename',
            '        sample_name = raw_file.stem',
            '        sample5_path = Path(output_folder) / f"{sample_name}.sample5"',
            '        ',
            '        # Skip if sample5 already exists',
            '        if sample5_path.exists() and not PARAMS["force_reprocess"]:',
            '            print(f"  Skipping {raw_file.name} (sample5 already exists)")',
            '            return str(sample5_path)',
            '        ',
            '        print(f"  Converting {raw_file.name}...")',
            '        ',
            '        # Load and process raw file with full pipeline',
            '        sample = Sample(log_label=sample_name)',
            '        sample.load(filename=str(raw_file))',
            '        sample.find_features(',
            '            noise=PARAMS["noise"],',
            '            chrom_fwhm=PARAMS["chrom_fwhm"],',
            '            chrom_peak_snr=PARAMS["chrom_peak_snr"]',
            '        )',
            '        sample.find_ms2()',
            '        sample.find_iso()',
            '        # sample.export_mgf()',
            '        # sample.plot_2d(filename=f"{sample5_path.replace(".sample5", ".html")}")',
            '        sample.save(str(sample5_path))',
            '        ',
            '        # print(f"  Completed {raw_file.name} -> {sample5_path.name}")',
            '        return str(sample5_path)',
            '        ',
            '    except Exception as e:',
            '        print(f"  ERROR processing {raw_file.name}: {e}")',
            '        return None',
            '',
            '',
            'def convert_raw_to_sample5(raw_files, output_folder, polarity, num_cores):',
            '    """Convert raw data files to sample5 format."""',
            '    import concurrent.futures',
            '    import os',
            '    ',
            '    # Create output directory',
            '    os.makedirs(output_folder, exist_ok=True)',
            '    ',
            '    # Prepare arguments for multiprocessing',
            '    file_args = [(raw_file, output_folder) for raw_file in raw_files]',
            '    ',
            '    # Process files in parallel',
            '    sample5_files = []',
            '    with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:',
            '        futures = [executor.submit(process_single_file, args) for args in file_args]',
            '        ',
            '        for future in concurrent.futures.as_completed(futures):',
            '            result = future.result()',
            '            if result:',
            '                sample5_files.append(result)',
            '    ',
            '    return sample5_files',
            '',
            '',
            'def main():',
            '    """Main analysis pipeline."""',
            '    try:',
            '        print("=" * 70)',
            f'        print("masster {version} - Automated MS Data Analysis")',
            '        print("=" * 70)',
            '        print(f"Source: {PARAMS[\'source\']}")',
            '        print(f"Output: {PARAMS[\'folder\']}")',
            '        print(f"Polarity: {PARAMS[\'polarity\']}")',
            '        print(f"CPU Cores: {PARAMS[\'num_cores\']}")',
            '        print("=" * 70)',
            '        ',
            '        start_time = time.time()',
            '        ',
            '        # Step 1: Discover raw data files',
            '        print("\\nStep 1/7: Discovering raw data files...")',
            '        raw_files = discover_raw_files(',
            '            PARAMS[\'source\'],',
            '            PARAMS[\'file_extensions\'],',
            '            PARAMS[\'search_subfolders\']',
            '        )',
            '        ',
            '        if not raw_files:',
            '            print("No raw data files found!")',
            '            return False',
            '        ',
            '        print(f"Found {len(raw_files)} raw data files")',
            '        for f in raw_files[:5]:  # Show first 5 files',
            '            print(f"  {f.name}")',
            '        if len(raw_files) > 5:',
            '            print(f"  ... and {len(raw_files) - 5} more")',
            '        ',
            '        # Step 2: Process raw files',
            '        print("\\nStep 2/7: Processing raw files...")',
            '        sample5_files = convert_raw_to_sample5(',
            '            raw_files,',
            '            PARAMS[\'folder\'],',
            '            PARAMS[\'polarity\'],',
            '            PARAMS[\'num_cores\']',
            '        )',
            '        ',
            '        if not sample5_files:',
            '            print("No sample5 files were created!")',
            '            return False',
            '        ',
            '        print(f"Successfully processed {len(sample5_files)} files to sample5")',
            '        ',
            '        # Step 3: Create and configure study',
            '        print("\\nStep 3/7: Initializing study...")',
            '        study = Study(folder=PARAMS[\'folder\'])',
            '        study.polarity = PARAMS[\'polarity\']',
            '        study.adducts = PARAMS[\'adducts\']',
            '        ',
            '        # Step 4: Add sample5 files to study',
            '        print("\\nStep 4/7: Adding samples to study...")',
            '        study.add(str(Path(PARAMS[\'folder\']) / "*.sample5"))',
            '        study.features_filter(study.features_select(chrom_coherence=0.1, chrom_prominence_scaled=1))',
            '        ',
            '        # Step 5: Core processing',
            '        print("\\nStep 5/7: Processing...")',
            '        study.align(',
            '            algorithm=PARAMS[\'alignment_method\'],',
            '            rt_tol=PARAMS[\'rt_tol\']',
            '        )',
            '        ',
            '        study.merge(',
            '            method="qt",',
            '            min_samples=PARAMS[\'min_samples_per_feature\'],',
            '            threads=PARAMS[\'num_cores\'],',
            '            rt_tol=PARAMS[\'rt_tol\']',
            '        )',
            '        study.find_iso()',
            '        study.fill()',
            '        study.integrate()',
            '        ',
            '        # Step 6/7: Saving results',
            '        print("\\nStep 6/7: Saving results...")',
            '        study.save()',
            '        study.export_xlsx()',
            '        study.export_mgf()',
            '        study.export_mztab()',
            '        ',
            '        # Step 7: Plots',
            '        print("\\nStep 7/7: Exporting plots...")',
            '        study.plot_consensus_2d(filename="consensus.html")',
            '        study.plot_consensus_2d(filename="consensus.png")',
            '        study.plot_alignment(filename="alignment.html")',
            '        study.plot_alignment(filename="alignment.png")',
            '        study.plot_samples_pca(filename="pca.html")',
            '        study.plot_samples_pca(filename="pca.png")',
            '        study.plot_bpc(filename="bpc.html")',
            '        study.plot_bpc(filename="bpc.png")',
            '        study.plot_rt_correction(filename="rt_correction.html")',
            '        study.plot_rt_correction(filename="rt_correction.png")',
            '        ',
            '        # Print summary',
            '        study.info()',
            '        total_time = time.time() - start_time',
            '        print("\\n" + "=" * 70)',
            '        print("ANALYSIS COMPLETE")',
            '        print("=" * 70)',
            '        print(f"Total processing time: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")',
            '        print(f"Raw files processed: {len(raw_files)}")',
            '        print(f"Sample5 files created: {len(sample5_files)}")',
            '        if hasattr(study, "consensus_df"):',
            '            print(f"Consensus features generated: {len(study.consensus_df)}")',
            '        print("=" * 70)',
            '        ',
            '        return True',
            '        ',
            '    except KeyboardInterrupt:',
            '        print("\\nAnalysis interrupted by user")',
            '        return False',
            '    except Exception as e:',
            '        print(f"Analysis failed with error: {e}")',
            '        import traceback',
            '        traceback.print_exc()',
            '        return False',
            '',
            '',
            'if __name__ == "__main__":',
            '    success = main()',
            '    sys.exit(0 if success else 1)',
        ]
        
        return '\n'.join(script_lines)

    def _generate_interactive_notebook_content(self, source_info: Dict[str, Any]) -> str:
        """Generate the content for 2_interactive_analysis.py marimo notebook."""
        
        notebook_lines = [
            'import marimo',
            '',
            '__generated_with = "0.9.14"',
            'app = marimo.App(width="medium")',
            '',
            '@app.cell',
            'def __():',
            '    import marimo as mo',
            '    return (mo,)',
            '',
            '@app.cell',
            'def __(mo):',
            '    mo.md(r"""',
            '    # MASSter Interactive Analysis',
            '    ',
            f'    **Source:** {source_info.get("number_of_files", 0)} files detected',
            f'    **Polarity:** {source_info.get("polarity", "unknown")}',
            '    ',
            '    This notebook provides interactive exploration of your processed study.',
            '    Make sure you have run `python 1_masster_workflow.py` first.',
            '    """)',
            '    return ()',
            '',
            '@app.cell',
            'def __():',
            '    import masster',
            '    return (masster,)',
            '',
            '@app.cell',
            'def __(masster):',
            '    study = masster.Study(folder=".")',
            '    return (study,)',
            '',
            '@app.cell',
            'def __(study):',
            '    study.info()',
            '    return ()',
            '',
            'if __name__ == "__main__":',
            '    app.run()',
        ]
        
        return '\n'.join(notebook_lines)

    def _generate_instructions(self, source_info: Dict[str, Any], files_created: List[str]) -> List[str]:
        """Generate usage instructions for the created scripts."""
        instructions = [f"Source analysis: {source_info.get('number_of_files', 0)} files found",
            f"Polarity detected: {source_info.get('polarity', 'unknown')}",
            "Files created:"]
        for file_path in files_created:
            instructions.append(f"  ✅ {str(Path(file_path).resolve())}")
        
        # Find the workflow script name from created files
        workflow_script_name = "1_masster_workflow.py"
        for file_path in files_created:
            if Path(file_path).name == "1_masster_workflow.py":
                workflow_script_name = Path(file_path).name
                break
            
        instructions.extend([
            "",
            "Next steps:",
            f"1. REVIEW PARAMETERS in {workflow_script_name}:",
            f"   In particular, verify the NOISE, CHROM_FWHM, and MIN_SAMPLES_FOR_MERGE",
            "",
            "2. EXECUTE SAMPLE PROCESSING:",
            f"   uv run python {workflow_script_name}",
            "",
            "3. INTERACTIVE ANALYSIS:",
            f"   uv run marimo edit {Path('2_interactive_analysis.py').name}",
            ""]            
        )
        
        return instructions

    def execute(self) -> Dict[str, Any]:
        """
        Execute the sample processing workflow.
        
        This method:
        1. Creates scripts if they don't exist (calls create_scripts())
        2. Runs the 1_masster_workflow.py script to process raw files
        
        Returns:
            Dictionary containing:
            - status: "success", "error", or "scripts_created"
            - message: Status message
            - instructions: List of next steps
            - files_created: List of created file paths (if scripts were created)
        """
        try:
            workflow_script_path = self.folder_path / "1_masster_workflow.py"
            
            # Check if workflow script exists, create it if not
            if not workflow_script_path.exists():
                print("📝 Workflow script not found, creating scripts first...")
                result = self.create_scripts()
                if result["status"] != "success":
                    return result
                
                print("✅ Scripts created successfully")
                print(f"📁 Output folder: {self.folder_path}")
                
            # Execute the workflow script
            print(f"🚀 Executing sample processing workflow...")
            print(f"📄 Running: {workflow_script_path.name}")
            print("=" * 60)
            
            import subprocess
            result = subprocess.run([
                sys.executable, str(workflow_script_path)
            ], cwd=str(self.folder_path))
            
            success = result.returncode == 0
            
            if success:
                print("=" * 60)
                print("✅ Sample processing completed successfully!")
                print("📋 Next step: Run interactive analysis")
                print("   uv run marimo edit 2_interactive_analysis.py")
                print("=" * 60)
                
                return {
                    "status": "success",
                    "message": "Sample processing completed successfully",
                    "instructions": [
                        "✅ Sample processing completed",
                        "Next: uv run marimo edit 2_interactive_analysis.py"
                    ],
                    "files_created": []
                }
            else:
                return {
                    "status": "error",
                    "message": f"Workflow execution failed with return code {result.returncode}",
                    "instructions": [
                        "❌ Check the error messages above",
                        "Review parameters in 1_masster_workflow.py",
                        f"Try running manually: python {workflow_script_path.name}"
                    ],
                    "files_created": []
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to execute workflow: {e}",
                "instructions": [
                    "❌ Execution failed",
                    "Check that source files exist and are accessible",
                    "Verify folder permissions"
                ],
                "files_created": []
            }

    def _generate_script_content(self) -> str:
        """Generate the complete analysis script content."""
        
        # Convert Path objects to strings for JSON serialization
        params_dict = {}
        for key, value in self.params.__dict__.items():
            if key == '_param_metadata':  # Skip metadata in generated script
                continue
            if isinstance(value, Path):
                params_dict[key] = str(value)
            else:
                params_dict[key] = value

        # Obtain list of files in source with extension wiff, .raw, .mzML
        raw_files = []
        for ext in params_dict.get('file_extensions', []):
            raw_files.extend(glob.glob(f"{params_dict.get('source', '')}/**/*{ext}", recursive=True))

        # Create readable PARAMS dict with comments
        params_lines = []
        params_lines.append('# Analysis parameters')
        params_lines.append('PARAMS = {')
        
        # Core Configuration
        params_lines.append('    # === Core Configuration ===')
        params_lines.append(f'    "source": {params_dict.get("source", "")!r},  # Directory containing raw data files')
        params_lines.append(f'    "folder": {params_dict.get("folder", "")!r},  # Output directory for processed study')
        params_lines.append(f'    "polarity": {params_dict.get("polarity", "positive")!r},  # Ion polarity mode ("positive" or "negative")')
        params_lines.append(f'    "num_cores": {params_dict.get("num_cores", 4)},  # Number of CPU cores for parallel processing')
        params_lines.append('')
        
        # File Discovery
        params_lines.append('    # === File Discovery ===')
        params_lines.append(f'    "file_extensions": {params_dict.get("file_extensions", [".wiff", ".raw", ".mzML"])!r},  # File extensions to search for')
        params_lines.append(f'    "search_subfolders": {params_dict.get("search_subfolders", True)},  # Whether to search subdirectories recursively')
        params_lines.append(f'    "skip_patterns": {params_dict.get("skip_patterns", ["blank", "condition"])!r},  # Filename patterns to skip')
        params_lines.append('')
        
        # Processing Parameters
        params_lines.append('    # === Processing Parameters ===')
        params_lines.append(f'    "adducts": {params_dict.get("adducts", [])!r},  # Adduct specifications for feature detection and annotation')
        params_lines.append(f'    "detector_type": {params_dict.get("detector_type", "unknown")!r},  # MS detector type ("orbitrap", "tof", "unknown")')
        params_lines.append(f'    "noise": {params_dict.get("noise", 50.0)},  # Noise threshold for feature detection')
        params_lines.append(f'    "chrom_fwhm": {params_dict.get("chrom_fwhm", 0.5)},  # Chromatographic peak full width at half maximum (seconds)')
        params_lines.append(f'    "chrom_peak_snr": {params_dict.get("chrom_peak_snr", 5.0)},  # Minimum signal-to-noise ratio for chromatographic peaks')
        params_lines.append('')
        
        # Alignment & Merging
        params_lines.append('    # === Alignment & Merging ===')
        params_lines.append(f'    "rt_tol": {params_dict.get("rt_tol", 2.0)},  # Retention time tolerance for alignment (seconds)')
        params_lines.append(f'    "mz_tol": {params_dict.get("mz_tol", 0.01)},  # Mass-to-charge ratio tolerance for alignment (Da)')
        params_lines.append(f'    "alignment_method": {params_dict.get("alignment_method", "kd")!r},  # Algorithm for sample alignment')
        params_lines.append(f'    "min_samples_per_feature": {params_dict.get("min_samples_per_feature", 1)},  # Minimum samples required per consensus feature')
        params_lines.append(f'    "merge_method": {params_dict.get("merge_method", "qt")!r},  # Method for merging consensus features')
        params_lines.append('')        

        # Sample Processing
        params_lines.append('    # === Sample Processing (used in add_samples_from_folder) ===')
        params_lines.append(f'    "batch_size": {params_dict.get("batch_size", 8)},  # Number of files to process per batch')
        params_lines.append(f'    "memory_limit_gb": {params_dict.get("memory_limit_gb", 16.0)},  # Memory limit for processing (GB)')
        params_lines.append('')        
        
        # Script Options
        params_lines.append('    # === Script Options ===')
        params_lines.append(f'    "resume_enabled": {params_dict.get("resume_enabled", True)},  # Enable automatic resume capability')
        params_lines.append(f'    "force_reprocess": {params_dict.get("force_reprocess", False)},  # Force reprocessing of existing files')
        params_lines.append(f'    "cleanup_temp_files": {params_dict.get("cleanup_temp_files", True)},  # Clean up temporary files after processing')
        
        params_lines.append('}')
        
        # Create script lines
        script_lines = [
            '#!/usr/bin/env python3',
            '"""',
            'Automated Mass Spectrometry Data Analysis Pipeline',
            f'Generated by masster wizard v{version}',
            '"""',
            '',
            'import sys',
            'import time',
            'from pathlib import Path',
            '',
            '# Import masster modules',
            'from masster.study import Study',
            'from masster import __version__',
            '',
        ]
        
        # Add the formatted PARAMS
        script_lines.extend(params_lines)
        
        # Add the main function and pipeline
        script_lines.extend([
            '',
            '',
            'def discover_raw_files(source_folder, file_extensions, search_subfolders=True):',
            '    """Discover raw data files in the source folder."""',
            '    source_path = Path(source_folder)',
            '    raw_files = []',
            '    ',
            '    for ext in file_extensions:',
            '        if search_subfolders:',
            '            pattern = f"**/*{ext}"',
            '            files = list(source_path.rglob(pattern))',
            '        else:',
            '            pattern = f"*{ext}"',
            '            files = list(source_path.glob(pattern))',
            '        raw_files.extend(files)',
            '    ',
            '    return raw_files',
            '',
            '',
            'def process_single_file(args):',
            '    """Process a single raw file to sample5 format - module level for multiprocessing."""',
            '    raw_file, output_folder = args',
            '    from masster.sample import Sample',
            '    ',
            '    try:',
            '        # Create sample5 filename',
            '        sample_name = raw_file.stem',
            '        sample5_path = Path(output_folder) / f"{sample_name}.sample5"',
            '        ',
            '        # Skip if sample5 already exists',
            '        if sample5_path.exists():',
            '            print(f"  Skipping {raw_file.name} (sample5 already exists)")',
            '            return str(sample5_path)',
            '        ',
            '        print(f"  Converting {raw_file.name}...")',
            '        ',
            '        # Load and process raw file with full pipeline',
            '        sample = Sample(log_label=sample_name)',
            '        sample.load(filename=str(raw_file))',
            '        sample.find_features(',
            '            noise=PARAMS[\'noise\'],',
            '            chrom_fwhm=PARAMS[\'chrom_fwhm\'],',
            '            chrom_peak_snr=PARAMS[\'chrom_peak_snr\']',
            '        )',
            '        sample.find_adducts(adducts=PARAMS[\'adducts\'])',
            '        sample.find_ms2()',
            '        # sample.find_iso()',
            '        # sample.export_mgf()',
            '        # sample.export_mztab()',
            '        # sample.plot_2d(filename="{sample_name}.html")',
            '        sample.save(str(sample5_path))',
            '        ',
            '        # print(f"  Completed {raw_file.name} -> {sample5_path.name}")',
            '        return str(sample5_path)',
            '        ',
            '    except Exception as e:',
            '        print(f"  ERROR processing {raw_file.name}: {e}")',
            '        return None',
            '',
            '',
            'def convert_raw_to_sample5(raw_files, output_folder, polarity, num_cores):',
            '    """Convert raw data files to sample5 format."""',
            '    import concurrent.futures',
            '    import os',
            '    ',
            '    # Create output directory',
            '    os.makedirs(output_folder, exist_ok=True)',
            '    ',
            '    # Prepare arguments for multiprocessing',
            '    file_args = [(raw_file, output_folder) for raw_file in raw_files]',
            '    ',
            '    # Process files in parallel',
            '    sample5_files = []',
            '    with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:',
            '        futures = [executor.submit(process_single_file, args) for args in file_args]',
            '        ',
            '        for future in concurrent.futures.as_completed(futures):',
            '            result = future.result()',
            '            if result:',
            '                sample5_files.append(result)',
            '    ',
            '    return sample5_files',
            '',
            '',
            'def main():',
            '    """Main analysis pipeline."""',
            '    try:',
            '        print("=" * 70)',
            f'        print("masster {version} - Automated MS Data Analysis")',
            '        print("=" * 70)',
            '        print(f"Source: {PARAMS[\'source\']}")',
            '        print(f"Output: {PARAMS[\'folder\']}")',
            '        print(f"Polarity: {PARAMS[\'polarity\']}")',
            '        print(f"CPU Cores: {PARAMS[\'num_cores\']}")',
            '        print("=" * 70)',
            '        ',
            '        start_time = time.time()',
            '        ',
            '        # Step 1: Discover raw data files',
            '        print("\\nStep 1/7: Discovering raw data files...")',
            '        raw_files = discover_raw_files(',
            '            PARAMS[\'source\'],',
            '            PARAMS[\'file_extensions\'],',
            '            PARAMS[\'search_subfolders\']',
            '        )',
            '        ',
            '        if not raw_files:',
            '            print("No raw data files found!")',
            '            return False',
            '        ',
            '        print(f"Found {len(raw_files)} raw data files")',
            '        for f in raw_files[:5]:  # Show first 5 files',
            '            print(f"  {f.name}")',
            '        if len(raw_files) > 5:',
            '            print(f"  ... and {len(raw_files) - 5} more")',
            '        ',
            '        # Step 2: Process raw files',
            '        print("\\nStep 2/7: Processing raw files...")',
            '        sample5_files = convert_raw_to_sample5(',
            '            raw_files,',
            '            PARAMS[\'folder\'],',
            '            PARAMS[\'polarity\'],',
            '            PARAMS[\'num_cores\']',
            '        )',
            '        ',
            '        if not sample5_files:',
            '            print("No sample5 files were created!")',
            '            return False',
            '        ',
            '        print(f"Successfully processed {len(sample5_files)} files to sample5")',
            '        ',
            '        # Step 3: Create and configure study',
            '        print("\\nStep 3/7: Initializing study...")',
            '        study = Study(folder=PARAMS[\'folder\'])',
            '        study.polarity = PARAMS[\'polarity\']',
            '        study.adducts = PARAMS[\'adducts\']',
            '        ',
            '        # Step 4: Add sample5 files to study',
            '        print("\\nStep 4/7: Adding samples to study...")',
            '        study.add(str(Path(PARAMS[\'folder\']) / "*.sample5"))',
            '        study.features_filter(study.features_select(chrom_coherence=0.1, chrom_prominence_scaled=1))',
            '        ',
            '        # Step 5: Core processing',
            '        print("\\nStep 5/7: Processing...")',
            '        study.align(',
            '            algorithm=PARAMS[\'alignment_method\'],',
            '            rt_tol=PARAMS[\'rt_tol\']',
            '        )',
            '        ',
            '        study.merge(',
            '            method="qt",',
            '            min_samples=PARAMS[\'min_samples_per_feature\'],',
            '            threads=PARAMS[\'num_cores\'],',
            '            rt_tol=PARAMS[\'rt_tol\'],'
            '        )',
            '        study.find_iso()',
            '        study.fill()',
            '        study.integrate()',    
            '        ',
            '        # Step 6/7: Saving results',
            '        print("\\nStep 6/7: Saving results...")',
            '        study.save()',
            '        study.export_xlsx()',
            '        study.export_mgf()',
            '        study.export_mztab()',
            '        ',
            '        # Step 7: Plots',
            '        print("\\nStep 7/7: Exporting plots...")',
            '        study.plot_consensus_2d(filename="consensus.html")',
            '        study.plot_consensus_2d(filename="consensus.png")',
            '        study.plot_alignment(filename="alignment.html")',
            '        study.plot_alignment(filename="alignment.png")',
            '        study.plot_samples_pca(filename="pca.html")',
            '        study.plot_samples_pca(filename="pca.png")',
            '        study.plot_bpc(filename="bpc.html")',
            '        study.plot_bpc(filename="bpc.png")',
            '        study.plot_rt_correction(filename="rt_correction.html")',
            '        study.plot_rt_correction(filename="rt_correction.png")',

            '        ',
            '        # Print summary',
            '        study.info()',
            '        total_time = time.time() - start_time',
            '        print("\\n" + "=" * 70)',
            '        print("ANALYSIS COMPLETE")',
            '        print("=" * 70)',
            '        print(f"Total processing time: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")',
            '        print(f"Raw files processed: {len(raw_files)}")',
            '        print(f"Sample5 files created: {len(sample5_files)}")',
            '        if hasattr(study, "consensus_df"):',
            '            print(f"Consensus features generated: {len(study.consensus_df)}")',
            '        print("=" * 70)',
            '        ',
            '        return True',
            '        ',
            '    except KeyboardInterrupt:',
            '        print("\\nAnalysis interrupted by user")',
            '        return False',
            '    except Exception as e:',
            '        print(f"Analysis failed with error: {e}")',
            '        import traceback',
            '        traceback.print_exc()',
            '        return False',
            '',
            '',
            'if __name__ == "__main__":',
            '    success = main()',
            '    sys.exit(0 if success else 1)',
        ])
        
        return '\n'.join(script_lines)


def create_script(
    source: str, 
    folder: str, 
    filename: str = 'run_masster.py', 
    polarity: str = "positive",
    adducts: Optional[List[str]] = None,
    params: Optional[wizard_def] = None,
    num_cores: int = 0,
    **kwargs
) -> bool:
    """
    Create a standalone analysis script without initializing a Wizard instance.
    
    This function generates a Python script that replicates automated processing
    steps with the specified configuration. The script can be executed independently
    to perform the same analysis.
    
    Parameters:
        source: Directory containing raw data files
        folder: Output directory for processed study  
        filename: Filename for the generated script (should end with .py)
        polarity: Ion polarity mode ("positive" or "negative")
        adducts: List of adduct specifications (auto-set if None)
        params: Custom wizard_def parameters (optional)
        num_cores: Number of CPU cores (0 = auto-detect)
        **kwargs: Additional parameters to override defaults
        
    Returns:
        True if script was generated successfully, False otherwise
        
    Example:
        >>> from masster.wizard import create_script
        >>> create_script(
        ...     source=r'D:\\Data\\raw_files',
        ...     folder=r'D:\\Data\\output', 
        ...     filename='run_masster.py',
        ...     polarity='positive'
        ... )
    """
    
    try:
        # Create parameters
        if params is not None:
            # Use provided params as base
            wizard_params = params
            # Update with provided values
            wizard_params.source = source
            wizard_params.folder = folder
            if polarity != "positive":  # Only override if explicitly different
                wizard_params.polarity = polarity
            if num_cores > 0:
                wizard_params.num_cores = num_cores
            if adducts is not None:
                wizard_params.adducts = adducts
        else:
            # Create new params with provided values
            wizard_params = wizard_def(
                source=source,
                folder=folder,
                polarity=polarity,
                num_cores=max(1, int(multiprocessing.cpu_count() * 0.75)) if num_cores <= 0 else num_cores
            )
            
            if adducts is not None:
                wizard_params.adducts = adducts
            
            # Apply any additional kwargs
            for key, value in kwargs.items():
                if hasattr(wizard_params, key):
                    setattr(wizard_params, key, value)
        
        # Ensure study folder exists
        study_path = Path(folder)
        study_path.mkdir(parents=True, exist_ok=True)
        
        # Create a temporary Wizard instance to generate the script
        temp_wizard = Wizard(params=wizard_params)
        
        # Generate the scripts using the instance method
        result = temp_wizard.create_scripts()
        success = result.get("status") == "success"
        
        return success
        
    except Exception as e:
        print(f"Failed to create script: {e}")
        import traceback
        traceback.print_exc()
        return False


def execute(
    source: str, 
    folder: str, 
    filename: str = 'run_masster.py', 
    polarity: str = "positive",
    adducts: Optional[List[str]] = None,
    params: Optional[wizard_def] = None,
    num_cores: int = 0,
    **kwargs
) -> bool:
    """
    Create and execute a standalone analysis script for automated MS data processing.
    
    This function generates a Python script with the same parameters as create_script(),
    but immediately executes it after creation. Combines script generation and execution
    in a single step.
    
    Parameters:
        source: Directory containing raw data files
        folder: Output directory for processed study  
        filename: Filename for the generated script (should end with .py)
        polarity: Ion polarity mode ("positive" or "negative")
        adducts: List of adduct specifications (auto-set if None)
        params: Custom wizard_def parameters (optional)
        num_cores: Number of CPU cores (0 = auto-detect)
        **kwargs: Additional parameters to override defaults
        
    Returns:
        True if script was created and executed successfully, False otherwise
        
    Example:
        >>> from masster.wizard import execute
        >>> execute(
        ...     source=r'D:\\Data\\raw_files',
        ...     folder=r'D:\\Data\\output', 
        ...     polarity='positive'
        ... )
    """
    
    try:
        # First, create the script using create_script()
        script_created = create_script(
            source=source,
            folder=folder,
            filename=filename,
            polarity=polarity,
            adducts=adducts,
            params=params,
            num_cores=num_cores,
            **kwargs
        )
        
        if not script_created:
            print("Failed to create analysis script")
            return False
            
        # Get the full path to the created script
        study_path = Path(folder)
        script_path = study_path / Path(filename).name
        
        if not script_path.exists():
            print(f"Script file not found: {script_path}")
            return False
            
        print(f"Executing...")
        #print("=" * 70)
        
        # Execute the script using subprocess with real-time output
        import subprocess
        
        # Run the script with Python, letting it inherit our stdout/stderr
        try:
            # Use subprocess.run for direct output inheritance - no capturing/re-printing
            result = subprocess.run([
                sys.executable, str(script_path)
            ], cwd=str(study_path))
            
            return_code = result.returncode
            
        except Exception as e:
            print(f"Error during script execution: {e}")
            return False
        
        success = return_code == 0
        
        if success:
            print("=" * 70)
            print("Script execution completed successfully")
        else:
            print("=" * 70)
            print(f"Script execution failed with return code: {return_code}")
            
        return success
        
    except Exception as e:
        print(f"Failed to execute script: {e}")
        import traceback
        traceback.print_exc()
        return False


def create_scripts(
    source: str = "", 
    folder: str = "", 
    polarity: str = "positive",
    adducts: Optional[List[str]] = None,
    num_cores: int = 0,
    **kwargs
) -> Dict[str, Any]:
    """
    Create analysis scripts without explicitly instantiating a Wizard.
    
    This is a convenience function that creates a Wizard instance internally
    and calls its create_scripts() method.
    
    Parameters:
        source: Directory containing raw data files
        folder: Output directory for processed study
        polarity: Ion polarity mode ("positive" or "negative")
        adducts: List of adduct specifications (auto-set if None)
        num_cores: Number of CPU cores (0 = auto-detect)
        **kwargs: Additional parameters
        
    Returns:
        Dictionary containing:
        - status: "success" or "error"
        - message: Status message
        - instructions: List of next steps
        - files_created: List of created file paths
        - source_info: Metadata about source files
        
    Example:
        >>> import masster.wizard
        >>> result = masster.wizard.create_scripts(
        ...     source=r'D:\\Data\\raw_files',
        ...     folder=r'D:\\Data\\output', 
        ...     polarity='negative'
        ... )
        >>> print("Status:", result["status"])
    """
    
    try:
        # Auto-detect optimal number of cores if not specified
        if num_cores <= 0:
            num_cores = max(1, int(multiprocessing.cpu_count() * 0.75))
        
        # Create Wizard instance
        wizard = Wizard(
            source=source,
            folder=folder,
            polarity=polarity,
            adducts=adducts,
            num_cores=num_cores,
            **kwargs
        )
        
        # Call the instance method
        return wizard.create_scripts()
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create scripts: {e}",
            "instructions": [],
            "files_created": [],
            "source_info": {}
        }


# Export the main classes and functions
__all__ = ["Wizard", "wizard_def", "create_scripts"]
