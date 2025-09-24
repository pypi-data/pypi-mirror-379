"""
Process commands for PDF processing and ingestion
"""

import click
import json
from pathlib import Path
from typing import Optional, List
import os
import sys

# Import processing modules
try:
    from ...hybrid_processor import process_pdf_hybrid
    from ...pdf_utils import check_pdf_page_count

    class PDFProcessor:
        """Wrapper class to interface with process_pdf_hybrid function"""
        def __init__(self, model_name=None, network_model=None, flow_model=None,
                     keep_images=False, image_width=1024, verbose=False, debug=False):
            self.model_name = model_name or "nanonets-ocr-s:latest"
            self.network_model = network_model
            self.flow_model = flow_model
            self.keep_images = keep_images
            self.image_width = image_width
            self.verbose = verbose
            self.debug = debug

        def process_pdf(self, file_path, start_page=None, end_page=None, **options):
            """Process a PDF file using hybrid processor with multi-model support"""
            import tempfile
            import os

            # Create temporary output directory
            output_dir = tempfile.mkdtemp(prefix='netintel_')

            try:
                # Get actual page count
                total_pages = check_pdf_page_count(file_path)

                # Call hybrid processor with multi-model configuration and all options
                process_pdf_hybrid(
                    pdf_path=file_path,
                    output_dir=output_dir,
                    model=self.model_name,
                    network_model=options.get('network_model', self.network_model),
                    flow_model=options.get('flow_model', self.flow_model),
                    keep_images=self.keep_images or options.get('keep_images', False),
                    width=self.image_width,
                    start=start_page or 1,
                    end=end_page or total_pages,
                    auto_detect=options.get('auto_detect', not options.get('text_only', False)),
                    confidence_threshold=options.get('confidence_threshold', 0.7),
                    use_icons=options.get('detect_icons', True),
                    fast_mode=options.get('text_only', False) or options.get('fast_mode', False),
                    timeout_seconds=options.get('timeout', 60),
                    include_text_with_diagrams=not options.get('diagram_only', False),
                    fast_extraction=options.get('fast_extraction', False),
                    force_multi_diagram=options.get('multi_diagram', False),
                    debug=self.debug or options.get('debug', False),
                    quiet=options.get('quiet', not self.verbose),
                    resume=options.get('resume', False),
                    extract_tables=options.get('extract_tables', True),
                    table_confidence=options.get('table_confidence', 0.7),
                    table_method=options.get('table_method', 'hybrid'),
                    save_table_json=options.get('save_table_json', False),
                    generate_vector=not options.get('no_vector', False),
                    vector_format=options.get('vector_format', 'milvus'),
                    chunk_size=options.get('chunk_size', 1000),
                    chunk_overlap=options.get('chunk_overlap', 100),
                    chunk_strategy=options.get('chunk_strategy', 'semantic')
                )

                # Read results from output directory
                import json
                from pathlib import Path

                output_path = Path(output_dir)

                # Find the MD5 subdirectory
                subdirs = list(output_path.glob("*/"))
                if subdirs:
                    md5_dir = subdirs[0]
                    markdown_dir = md5_dir / "markdown"

                    # Read the merged document
                    merged_file = markdown_dir / "document.md"
                    if merged_file.exists():
                        with open(merged_file, 'r') as f:
                            text = f.read()
                    else:
                        text = ""

                    # Count network diagrams
                    network_diagrams = len(list(markdown_dir.glob("*network*.md")))

                    # Count tables
                    tables_dir = md5_dir / "tables"
                    tables = len(list(tables_dir.glob("*.json"))) if tables_dir.exists() else 0

                    return {
                        'text': text,
                        'pages_processed': end_page - (start_page or 1) + 1 if end_page else total_pages,
                        'network_diagrams': network_diagrams,
                        'tables': tables,
                        'output_path': str(md5_dir)
                    }
                else:
                    return {
                        'text': '',
                        'pages_processed': 0,
                        'error': 'No output generated'
                    }

            finally:
                # Cleanup temp directory if not keeping images
                if not self.keep_images:
                    import shutil
                    if os.path.exists(output_dir):
                        try:
                            shutil.rmtree(output_dir)
                        except:
                            pass

except ImportError as e:
    # Fallback placeholder if hybrid_processor is not available
    class PDFProcessor:
        def __init__(self, **kwargs):
            self.error = str(e)
        def process_pdf(self, *args, **kwargs):
            return {'text': f'Error: {self.error}', 'pages_processed': 0}

try:
    from ...dedup import DedupManager, DedupMode
except ImportError:
    # Placeholder for missing module
    from enum import Enum

    class DedupMode(Enum):
        EXACT = 'exact'
        FUZZY = 'fuzzy'
        HYBRID = 'hybrid'
        FULL = 'full'
    class DedupManager:
        def __init__(self, **kwargs):
            pass
        def is_duplicate(self, text):
            return False
        def add_document(self, text, metadata):
            pass
        def get_stats(self):
            return {'total_documents': 0, 'unique_documents': 0, 'duplicates_found': 0}

try:
    from ...utils.checkpoint import CheckpointManager
except ImportError:
    # Placeholder for missing module
    class CheckpointManager:
        def __init__(self, path):
            self.path = path
            self.data = {}
        def load(self):
            pass
        def save(self):
            pass
        def get_processed_files(self):
            return []
        def get_remaining_files(self):
            return []
        def mark_processed(self, file):
            pass


@click.group()
def process():
    """Process PDF documents"""
    pass


@process.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(),
              help='Output file path')
@click.option('--model', '-m', default=None,
              help='OCR model to use for text extraction (e.g., nanonets-ocr-s:latest)')
@click.option('--network-model', default=None,
              help='Model for network diagram processing. If not specified, uses --model. '
                   'Recommended: qwen2.5vl for diagrams, nanonets-ocr-s for text. '
                   'Example: --model nanonets-ocr-s --network-model qwen2.5vl')
@click.option('--flow-model', default=None,
              help='Model for flow diagram processing. If not specified, uses --network-model or --model')
@click.option('--text-only', '-t', is_flag=True,
              help='Text-only mode: Skip network diagram detection for faster processing')
@click.option('--network-only', is_flag=True,
              help='Process ONLY network diagrams, skip regular text pages')
@click.option('--pages', type=str,
              help='Page range (e.g., 1-10 or 1,3,5)')
@click.option('--start', '-s', type=int, default=None,
              help='Start page number')
@click.option('--end', '-e', type=int, default=None,
              help='End page number')
@click.option('--confidence', '-c', type=float, default=0.7,
              help='Network diagram detection confidence threshold (0.0 to 1.0)')
@click.option('--no-icons', is_flag=True,
              help='Disable Font Awesome icons in Mermaid diagrams')
@click.option('--diagram-only', is_flag=True,
              help='On pages with network diagrams, only extract the diagram without page text')
@click.option('--fast-extraction', is_flag=True,
              help='Use optimized fast extraction for network diagrams (50-70% faster)')
@click.option('--multi-diagram', is_flag=True,
              help='Force multi-diagram extraction mode for complex pages')
@click.option('--no-auto-detect', is_flag=True,
              help='Disable automatic network diagram detection (process as text only)')
@click.option('--extract-tables', is_flag=True, default=True,
              help='Extract tables from PDF (enabled by default)')
@click.option('--no-tables', is_flag=True,
              help='Disable table extraction for faster processing')
@click.option('--table-confidence', type=float, default=0.7,
              help='Table detection confidence threshold')
@click.option('--table-method', type=click.Choice(['llm', 'hybrid']), default='hybrid',
              help='Table extraction method')
@click.option('--save-table-json', is_flag=True,
              help='Save extracted tables as separate JSON files')
@click.option('--resume', is_flag=True,
              help='Resume processing from a checkpoint if one exists')
@click.option('--timeout', type=int, default=60,
              help='Timeout for each LLM operation in seconds')
@click.option('--keep-images', '-k', is_flag=True,
              help='Keep intermediate image files')
@click.option('--width', '-w', type=int, default=1024,
              help='Image width for processing')
@click.option('--debug', '-d', is_flag=True,
              help='Enable debug output with detailed processing information')
@click.option('--verbose', '-v', is_flag=True,
              help='Verbose output - show progress information')
@click.option('--quiet', '-q', is_flag=True,
              help='Quiet mode - minimal output')
@click.option('--with-kg', is_flag=True,
              help='Enable knowledge graph extraction')
@click.option('--kg-model', default='RotatE',
              help='Knowledge graph embedding model')
@click.option('--no-vector', is_flag=True,
              help='Disable vector generation (enabled by default)')
@click.option('--vector-format', type=str, default='milvus',
              help='Vector database format (default: milvus)')
@click.option('--chunk-size', type=int, default=1000,
              help='Chunk size for vector generation')
@click.option('--chunk-overlap', type=int, default=100,
              help='Chunk overlap for vector generation')
@click.option('--chunk-strategy', type=click.Choice(['semantic', 'fixed', 'sentence']),
              default='semantic', help='Chunking strategy for vectors')
@click.pass_context
def file(ctx, file_path, output, model, network_model, flow_model, text_only, network_only, pages,
         start, end, confidence, no_icons, diagram_only, fast_extraction, multi_diagram,
         no_auto_detect, extract_tables, no_tables, table_confidence, table_method,
         save_table_json, resume, timeout, keep_images, width, debug, verbose, quiet,
         with_kg, kg_model, no_vector, vector_format, chunk_size, chunk_overlap, chunk_strategy):
    """Process a single PDF file with multi-model support"""

    # Handle conflicting verbose/quiet options
    if quiet and verbose:
        click.echo("Cannot use both --quiet and --verbose", err=True)
        sys.exit(1)

    # Set debug and verbose in context if needed
    if not ctx.obj:
        ctx.obj = type('obj', (object,), {'debug': debug, 'verbose': verbose})()
    else:
        ctx.obj.debug = ctx.obj.debug or debug
        ctx.obj.verbose = ctx.obj.verbose or verbose

    if not quiet:
        click.echo(f"Processing: {file_path}")

    # Parse page range - prioritize --start/--end over --pages
    start_page = start
    end_page = end
    if pages and not (start or end):
        if '-' in pages:
            parts = pages.split('-')
            start_page = int(parts[0])
            end_page = int(parts[1])
        elif ',' in pages:
            click.echo("Page lists not yet supported, use range format (1-10)", err=True)
            sys.exit(1)

    # Handle table options
    extract_tables_flag = extract_tables and not no_tables

    # Handle auto-detect
    auto_detect = not no_auto_detect and not text_only

    # Configure processor with multi-model support
    processor = PDFProcessor(
        model_name=model,
        network_model=network_model,
        flow_model=flow_model,
        keep_images=keep_images,
        image_width=width,
        verbose=verbose or (ctx.obj.verbose if ctx.obj else False),
        debug=debug or (ctx.obj.debug if ctx.obj else False)
    )

    # Process options with all parameters
    options = {
        'text_only': text_only,
        'network_only': network_only,
        'auto_detect': auto_detect,
        'detect_icons': not no_icons,
        'confidence_threshold': confidence,
        'diagram_only': diagram_only,
        'fast_extraction': fast_extraction,
        'multi_diagram': multi_diagram,
        'extract_tables': extract_tables_flag,
        'table_confidence': table_confidence,
        'table_method': table_method,
        'save_table_json': save_table_json,
        'resume': resume,
        'timeout': timeout,
        'fast_mode': text_only,
        'enable_kg': with_kg,
        'kg_model': kg_model,
        'network_model': network_model,
        'flow_model': flow_model,
        'debug': debug,
        'verbose': verbose,
        'quiet': quiet,
        'no_vector': no_vector,
        'vector_format': vector_format,
        'chunk_size': chunk_size,
        'chunk_overlap': chunk_overlap,
        'chunk_strategy': chunk_strategy,
        'keep_images': keep_images
    }

    # Show multi-model configuration if verbose
    if verbose:
        click.echo(f"   • Text model: {model or 'default'}")
        if network_model:
            click.echo(f"   • Network model: {network_model}")
        if flow_model:
            click.echo(f"   • Flow model: {flow_model}")
        if extract_tables_flag:
            click.echo(f"   • Table extraction: enabled (method: {table_method})")
        if not no_vector:
            click.echo(f"   • Vector generation: enabled (format: {vector_format})")

    try:
        # Process PDF
        results = processor.process_pdf(
            file_path,
            start_page=start_page,
            end_page=end_page,
            **options
        )

        # Save results
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if output_path.suffix == '.json':
                with open(output_path, 'w') as f:
                    json.dump(results, f, indent=2, default=str)
            else:
                # Default to JSON
                with open(output_path, 'w') as f:
                    json.dump(results, f, indent=2, default=str)

            click.echo(f"✅ Results saved to: {output}")
        else:
            # Print summary
            click.echo("\n📊 Processing Summary:")
            click.echo(f"   • Pages processed: {results.get('pages_processed', 0)}")
            click.echo(f"   • Text extracted: {len(results.get('text', '').split())} words")
            if 'network_diagrams' in results:
                click.echo(f"   • Network diagrams: {len(results['network_diagrams'])}")
            if 'tables' in results:
                click.echo(f"   • Tables: {len(results['tables'])}")

            if ctx.obj and ctx.obj.verbose:
                click.echo("\n📝 Full results:")
                click.echo(json.dumps(results, indent=2, default=str))

    except Exception as e:
        click.echo(f"❌ Error processing file: {e}", err=True)
        if ctx.obj and ctx.obj.debug:
            raise
        sys.exit(1)


@process.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--files', type=click.Path(exists=True),
              help='Text file containing list of PDFs to process')
@click.option('--pattern', default='*.pdf',
              help='File pattern to match (default: *.pdf)')
@click.option('--parallel', type=int, default=4,
              help='Number of parallel workers')
@click.option('--checkpoint', type=click.Path(),
              help='Checkpoint file for resuming')
@click.option('--output-dir', type=click.Path(),
              help='Output directory for results')
@click.option('--dedup', is_flag=True,
              help='Enable deduplication')
@click.option('--model', '-m', default=None,
              help='OCR model to use for text extraction')
@click.option('--network-model', default=None,
              help='Model for network diagram processing')
@click.option('--flow-model', default=None,
              help='Model for flow diagram processing')
@click.pass_context
def batch(ctx, path, files, pattern, parallel, checkpoint, output_dir, dedup, model, network_model, flow_model):
    """Process multiple PDF files in batch"""

    # Collect PDF files
    pdf_files = []

    if files:
        # Read from file list
        with open(files, 'r') as f:
            pdf_files = [line.strip() for line in f if line.strip()]
    else:
        # Scan directory
        path = Path(path)
        if path.is_file():
            pdf_files = [str(path)]
        else:
            import glob
            pdf_files = glob.glob(str(path / pattern))

    if not pdf_files:
        click.echo("No PDF files found to process", err=True)
        sys.exit(1)

    click.echo(f"📚 Found {len(pdf_files)} PDF files to process")

    # Setup checkpoint if requested
    checkpoint_mgr = None
    if checkpoint:
        checkpoint_mgr = CheckpointManager(checkpoint)
        checkpoint_mgr.load()

        # Filter already processed files
        processed = checkpoint_mgr.get_processed_files()
        pdf_files = [f for f in pdf_files if f not in processed]

        if processed:
            click.echo(f"   • Skipping {len(processed)} already processed files")

    # Setup output directory
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    # Setup deduplication
    dedup_mgr = None
    if dedup:
        dedup_mgr = DedupManager(mode=DedupMode.HYBRID)
        click.echo("   • Deduplication enabled (hybrid mode)")

    # Process files with multi-model support
    processor = PDFProcessor(
        model_name=model,
        network_model=network_model,
        flow_model=flow_model,
        verbose=ctx.obj.verbose if ctx.obj else False,
        debug=ctx.obj.debug if ctx.obj else False
    )

    # Show multi-model configuration if verbose
    if ctx.obj and ctx.obj.verbose:
        click.echo(f"   • Text model: {model or 'default'}")
        if network_model:
            click.echo(f"   • Network model: {network_model}")
        if flow_model:
            click.echo(f"   • Flow model: {flow_model}")

    from concurrent.futures import ThreadPoolExecutor, as_completed
    from tqdm import tqdm

    def process_single(pdf_path):
        """Process a single PDF"""
        try:
            results = processor.process_pdf(pdf_path)

            # Check for duplicates
            if dedup_mgr:
                text = results.get('text', '')
                if dedup_mgr.is_duplicate(text):
                    return pdf_path, None, "duplicate"

            # Save results if output directory specified
            if output_dir:
                output_file = output_dir / f"{Path(pdf_path).stem}_results.json"
                with open(output_file, 'w') as f:
                    json.dump(results, f, indent=2, default=str)

            return pdf_path, results, "success"

        except Exception as e:
            return pdf_path, None, str(e)

    # Process in parallel using threads (avoids pickle issues)
    successful = 0
    failed = 0
    duplicates = 0

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {executor.submit(process_single, pdf): pdf for pdf in pdf_files}

        with tqdm(total=len(pdf_files), desc="Processing") as pbar:
            for future in as_completed(futures):
                pdf_path, results, status = future.result()

                if status == "success":
                    successful += 1
                    if checkpoint_mgr:
                        checkpoint_mgr.mark_processed(pdf_path)
                elif status == "duplicate":
                    duplicates += 1
                else:
                    failed += 1
                    if ctx.obj and ctx.obj.verbose:
                        click.echo(f"\n❌ Failed: {pdf_path} - {status}", err=True)

                pbar.update(1)

    # Final summary
    click.echo("\n✅ Batch processing complete:")
    click.echo(f"   • Successful: {successful}")
    click.echo(f"   • Failed: {failed}")
    if dedup:
        click.echo(f"   • Duplicates: {duplicates}")

    if checkpoint_mgr:
        checkpoint_mgr.save()
        click.echo(f"   • Checkpoint saved: {checkpoint}")


@process.command()
@click.argument('folder', type=click.Path(exists=True))
@click.option('--pattern', default='*.pdf',
              help='File pattern to watch')
@click.option('--interval', type=int, default=60,
              help='Check interval in seconds')
@click.option('--output-dir', type=click.Path(),
              help='Output directory for results')
@click.option('--model', '-m', default=None,
              help='OCR model to use for text extraction')
@click.option('--network-model', default=None,
              help='Model for network diagram processing')
@click.option('--flow-model', default=None,
              help='Model for flow diagram processing')
@click.pass_context
def watch(ctx, folder, pattern, interval, output_dir, model, network_model, flow_model):
    """Watch folder for new PDFs and process them"""

    import time
    from pathlib import Path

    folder = Path(folder)
    if not folder.is_dir():
        click.echo(f"Error: {folder} is not a directory", err=True)
        sys.exit(1)

    click.echo(f"👁️  Watching: {folder}")
    click.echo(f"   • Pattern: {pattern}")
    click.echo(f"   • Interval: {interval}s")
    click.echo("   Press Ctrl+C to stop")

    # Setup output directory
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    # Track processed files
    processed = set()

    processor = PDFProcessor(
        model_name=model,
        network_model=network_model,
        flow_model=flow_model,
        verbose=ctx.obj.verbose if ctx.obj else False
    )

    # Show multi-model configuration if verbose
    if ctx.obj and ctx.obj.verbose:
        click.echo(f"   • Text model: {model or 'default'}")
        if network_model:
            click.echo(f"   • Network model: {network_model}")
        if flow_model:
            click.echo(f"   • Flow model: {flow_model}")

    try:
        while True:
            # Find PDF files
            import glob
            pdf_files = glob.glob(str(folder / pattern))

            # Process new files
            for pdf_path in pdf_files:
                if pdf_path not in processed:
                    click.echo(f"\n📄 Processing new file: {pdf_path}")

                    try:
                        results = processor.process_pdf(pdf_path)

                        if output_dir:
                            output_file = output_dir / f"{Path(pdf_path).stem}_results.json"
                            with open(output_file, 'w') as f:
                                json.dump(results, f, indent=2, default=str)
                            click.echo(f"   ✅ Saved to: {output_file}")

                        processed.add(pdf_path)

                    except Exception as e:
                        click.echo(f"   ❌ Error: {e}", err=True)

            # Wait for next check
            time.sleep(interval)

    except KeyboardInterrupt:
        click.echo("\n\n✋ Watch stopped")
        click.echo(f"   • Processed {len(processed)} files")


@process.command()
@click.argument('checkpoint_file', type=click.Path(exists=True))
@click.pass_context
def resume(ctx, checkpoint_file):
    """Resume processing from checkpoint"""

    checkpoint_mgr = CheckpointManager(checkpoint_file)
    checkpoint_mgr.load()

    remaining = checkpoint_mgr.get_remaining_files()
    if not remaining:
        click.echo("✅ All files already processed")
        return

    click.echo(f"📂 Resuming processing:")
    click.echo(f"   • Checkpoint: {checkpoint_file}")
    click.echo(f"   • Remaining files: {len(remaining)}")

    # Continue batch processing
    ctx.invoke(batch,
               path=".",  # Will be overridden by file list
               files=None,
               pattern="*.pdf",
               parallel=4,
               checkpoint=checkpoint_file,
               output_dir=checkpoint_mgr.data.get('output_dir'),
               dedup=checkpoint_mgr.data.get('dedup', False),
               model=checkpoint_mgr.data.get('model'))


@process.command()
@click.argument('checkpoint_file', type=click.Path(exists=True))
def status(checkpoint_file):
    """Show checkpoint status"""

    checkpoint_mgr = CheckpointManager(checkpoint_file)
    checkpoint_mgr.load()

    processed = checkpoint_mgr.get_processed_files()
    remaining = checkpoint_mgr.get_remaining_files()

    click.echo(f"📊 Checkpoint Status:")
    click.echo(f"   • File: {checkpoint_file}")
    click.echo(f"   • Processed: {len(processed)} files")
    click.echo(f"   • Remaining: {len(remaining)} files")

    if processed:
        click.echo("\n✅ Recently processed:")
        for f in list(processed)[-5:]:
            click.echo(f"   • {Path(f).name}")

    if remaining:
        click.echo("\n⏳ Next to process:")
        for f in list(remaining)[:5]:
            click.echo(f"   • {Path(f).name}")


@process.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['exact', 'fuzzy', 'hybrid', 'full']),
              default='hybrid',
              help='Deduplication mode')
@click.option('--threshold', type=int, default=5,
              help='Hamming distance threshold for fuzzy matching')
@click.option('--output', '-o', type=click.Path(),
              help='Output file for deduplicated content')
def dedup(file_path, mode, threshold, output):
    """Deduplicate content in PDF"""

    click.echo(f"🔍 Deduplicating: {file_path}")
    click.echo(f"   • Mode: {mode}")

    dedup_mgr = DedupManager(
        mode=DedupMode[mode.upper()],
        hamming_threshold=threshold
    )

    # Process PDF
    processor = PDFProcessor()
    results = processor.process_pdf(file_path)

    # Deduplicate text
    text = results.get('text', '')
    if not dedup_mgr.is_duplicate(text):
        dedup_mgr.add_document(text, metadata={'file': file_path})
        click.echo("   ✅ Content is unique")
    else:
        click.echo("   ⚠️  Duplicate content detected")

    # Show statistics
    stats = dedup_mgr.get_stats()
    click.echo(f"\n📊 Deduplication Stats:")
    click.echo(f"   • Total documents: {stats['total_documents']}")
    click.echo(f"   • Unique documents: {stats['unique_documents']}")
    click.echo(f"   • Duplicates found: {stats['duplicates_found']}")


@process.command(name='find-duplicates')
@click.argument('path', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['exact', 'fuzzy', 'hybrid']),
              default='hybrid',
              help='Deduplication mode')
@click.option('--output', '-o', type=click.Path(),
              help='Output file for duplicate report')
def find_duplicates(path, mode, output):
    """Find duplicate PDFs in directory"""

    import glob
    from pathlib import Path

    path = Path(path)
    if path.is_file():
        pdf_files = [str(path)]
    else:
        pdf_files = glob.glob(str(path / "*.pdf"))

    click.echo(f"🔍 Scanning for duplicates:")
    click.echo(f"   • Files: {len(pdf_files)}")
    click.echo(f"   • Mode: {mode}")

    dedup_mgr = DedupManager(mode=DedupMode[mode.upper()])
    processor = PDFProcessor()

    duplicates = []
    unique = []

    with click.progressbar(pdf_files, label='Processing') as files:
        for pdf_file in files:
            try:
                results = processor.process_pdf(pdf_file)
                text = results.get('text', '')

                if dedup_mgr.is_duplicate(text):
                    duplicates.append(pdf_file)
                else:
                    unique.append(pdf_file)
                    dedup_mgr.add_document(text, metadata={'file': pdf_file})

            except Exception as e:
                click.echo(f"\n❌ Error processing {pdf_file}: {e}", err=True)

    # Report results
    click.echo(f"\n📊 Duplicate Detection Results:")
    click.echo(f"   • Unique files: {len(unique)}")
    click.echo(f"   • Duplicate files: {len(duplicates)}")

    if duplicates:
        click.echo("\n🔁 Duplicates found:")
        for dup in duplicates[:10]:  # Show first 10
            click.echo(f"   • {Path(dup).name}")

        if len(duplicates) > 10:
            click.echo(f"   ... and {len(duplicates) - 10} more")

    # Save report if requested
    if output:
        report = {
            'mode': mode,
            'total_files': len(pdf_files),
            'unique_files': len(unique),
            'duplicate_files': len(duplicates),
            'unique': unique,
            'duplicates': duplicates
        }

        with open(output, 'w') as f:
            json.dump(report, f, indent=2)

        click.echo(f"\n✅ Report saved to: {output}")


@process.command(name='dedup-stats')
def dedup_stats():
    """Show deduplication statistics"""

    # This would connect to the dedup database
    click.echo("📊 Global Deduplication Statistics:")
    click.echo("   • Feature coming soon...")
    click.echo("   • Will show stats from dedup database")