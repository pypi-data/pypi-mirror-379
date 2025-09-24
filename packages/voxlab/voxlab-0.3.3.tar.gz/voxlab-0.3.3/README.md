# VoxLab

A comprehensive Python toolbox for audio processing using PyTorch. VoxLab provides a clean, device-aware architecture for audio manipulation with PyTorch tensors and supports GPU acceleration.

## Features

- **Device-Aware Audio Processing**: CPU/GPU operations with automatic device preservation
- **Memory-Efficient Operations**: In-place processing options to reduce memory usage
- **Comprehensive Preprocessing Pipeline**: Resampling, mono conversion, silence removal, chunking, and RMS normalization
<!-- - **Voice Embedding Extraction**: ECAPA2 model support via Hugging Face Hub (Coming Soon) -->
- **WebM Format Support**: Full support for WebM audio files via librosa fallback
- **Extensive Testing**: 84 passing tests covering all functionality

## Installation

### CUDA Installation (Recommended)
```bash
# Create conda environment with Python 3.11.13
conda create -n voxlab python=3.11.13 -y
conda activate voxlab

# Install PyTorch with CUDA 12.6 support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# Install in editable mode
pip install -e .
```

### CPU-Only Installation
```bash
# For CPU-only usage (no CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -e .
```

## Quick Start

### Basic Audio Processing
```python
from voxlab.core.audio_samples import AudioSamples
from voxlab.preprocessing.functions import resample_audio, convert_to_mono

# Load and process audio (supports wav, mp3, ogg, flac, webm)
audio = AudioSamples.load("input.webm")  # WebM files supported!
audio = resample_audio(audio, 16000, inplace=True)  # Memory efficient
audio = convert_to_mono(audio, method='left', inplace=True)
audio.export("output.wav")
```

### GPU-Accelerated Workflow
```python
# Move to GPU for processing
audio = AudioSamples.load("input.wav").cuda()
print(f"Audio device: {audio.device}")  # cuda:0

# All operations preserve GPU device
audio = resample_audio(audio, 16000, inplace=True)  # Stays on GPU
audio = normalize_audio_rms(audio, target_rms=-20, inplace=True)  # Stays on GPU
```

### Pipeline Processing
```python
from voxlab.preprocessing.pipeline import PreprocessingPipeline
from voxlab.preprocessing.functions import *

# Create pipeline
pipeline = PreprocessingPipeline()
pipeline.add_step(resample_audio, new_sample_rate=16000)
pipeline.add_step(convert_to_mono, method='left')
pipeline.add_step(normalize_audio_rms, target_rms=-15)

# Process (maintains device throughout)
audio = AudioSamples.load("input.wav").cuda()
result = pipeline.process(audio)  # Result stays on GPU
```

## Memory Management: In-Place vs Off-Place Operations

VoxLab offers flexible memory management through `inplace` parameters in all preprocessing functions. Choose the approach that best fits your workflow:

### Memory-Efficient In-Place Operations (Default)
Perfect for GPU workflows and memory-constrained environments:

```python
# Pipeline approach (recommended)
from voxlab.preprocessing.pipeline import PreprocessingPipeline
from voxlab.preprocessing.functions import *

pipeline = PreprocessingPipeline()
pipeline.add_step(resample_audio, new_sample_rate=16000)  # inplace=True default
pipeline.add_step(convert_to_mono, method='left')
pipeline.add_step(normalize_audio_rms, target_rms=-20)
pipeline.add_step(trim_audio, mode='both')

audio = AudioSamples.load("input.wav").cuda()
original_id = id(audio)
result = pipeline.process(audio)  # Single "run pipeline" action
assert id(result) == original_id  # Same object through entire pipeline!

print(f"Memory efficient: {audio.device}")  # Stays on GPU
```

### Immutable Off-Place Operations
Ideal for functional programming and data preservation:

```python
# Off-place operations (inplace=False)
original_audio = AudioSamples.load("input.wav")
resampled = resample_audio(original_audio, 16000, inplace=False)
mono = convert_to_mono(resampled, method='left', inplace=False)  
normalized = normalize_audio_rms(mono, target_rms=-20, inplace=False)

# Each operation creates a new object
assert id(original_audio) != id(resampled)
assert id(resampled) != id(mono) 
assert id(mono) != id(normalized)

# Original remains unchanged
print(f"Original: {original_audio.sample_rate}Hz, {original_audio.channels} channels")
print(f"Result: {normalized.sample_rate}Hz, {normalized.channels} channels")
```

### Mixed Workflow
Combine both approaches as needed:

```python
# Load and preserve original
original = AudioSamples.load("input.wav")

# Create working copy for in-place operations
working_copy = resample_audio(original, 16000, inplace=False)  # New object
working_copy = convert_to_mono(working_copy, inplace=True)     # Modify copy
working_copy = normalize_audio_rms(working_copy, inplace=True) # Modify copy

# Original untouched, working_copy efficiently processed
assert original.sample_rate != working_copy.sample_rate
```

### Pipeline Memory Behavior
Pipelines respect individual step `inplace` parameters:

```python
# Memory-efficient pipeline (default inplace=True)
pipeline = PreprocessingPipeline()
pipeline.add_step(resample_audio, new_sample_rate=16000)  # inplace=True default
pipeline.add_step(convert_to_mono, method='left')         # inplace=True default

audio = AudioSamples.load("input.wav")
original_id = id(audio)
result = pipeline.process(audio)
assert id(result) == original_id  # Same object through entire pipeline

# Immutable pipeline
pipeline = PreprocessingPipeline()
pipeline.add_step(resample_audio, new_sample_rate=16000, inplace=False)
pipeline.add_step(convert_to_mono, method='left', inplace=False)

result = pipeline.process(audio)
assert id(result) != id(audio)  # New object created
```

## Core Components

### AudioSamples Class
- Central data structure using PyTorch tensors
- Device-aware operations (`.cuda()`, `.cpu()`, `.to()`)
- Automatic format conversions and stereo handling
- Export to multiple formats (wav, mp3, ogg, flac)

### Preprocessing Functions
- **`resample_audio()`**: Device-preserving resampling with configurable sample rates
- **`convert_to_mono()`**: Stereo-to-mono conversion with channel selection
- **`remove_silence()`**: Intelligent silence removal with fade transitions
- **`break_into_chunks()`**: Audio segmentation with fade-in/fade-out
- **`normalize_audio_rms()`**: RMS-based normalization to target dB levels
- **`trim_audio()`**: Silence trimming from start, end, or both ends with configurable threshold

<!-- ### Embedding Extraction (Coming Soon)
- **ECAPA2Model**: State-of-the-art speaker embedding model
- **Extractor**: High-level interface for embedding extraction
- **GPU acceleration** with automatic device detection -->

## Testing

Run tests using pytest:
```bash
source venv/bin/activate  # or conda activate voxlab
pytest tests/ -v
```

**Current Status: ✅ 84 tests passing**
- AudioSamples core functionality (22 tests)
- Device awareness and GPU operations (12 tests)  
- Preprocessing functions (41 tests)
- Pipeline system (11 tests)
- Utilities and infrastructure (3 tests)

## Requirements

### Core Dependencies
- Python >= 3.11.13
- PyTorch >= 2.8.0 (with torchaudio)
- scipy >= 1.16.2
- numpy >= 2.1.2
- librosa >= 0.10.0 (for WebM support)
- pytest >= 8.4.2 (for testing)

<!-- ### ML Dependencies (Coming Soon)
- Hugging Face Hub >= 0.10.0
- transformers >= 4.0.0 -->

## License

MIT License

## Author

Rafaello Virgilli (rvirgilli@gmail.com)