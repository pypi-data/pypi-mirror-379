import argparse, tempfile, logging, os
from samplesheetutils.utils.sample import *
from samplesheetutils.utils.output import *
from samplesheetutils.utils.fasta import *
from samplesheetutils.utils.input import *

# Consts
MODE_STRING_CSV = 0
MODE_DIR_CSV = 1
MODE_STRING_JSON = 2
MODE_DIR_JSON = 3
MODE_STRING_YAML = 4
MODE_DIR_YAML = 5
MODE_STRING_YAML_RFAA = 8
MODE_DIR_YAML_RFAA = 9

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig()

def version():
    print("samplesheet-utils 1.3.3")

#if __name__ == "__main__":
def create_samplesheet():
    parser = argparse.ArgumentParser(
        prog="Create Samplesheet",
        description="Utility to create a samplesheet from directory, or AA string",
        epilog="Written by nbtm-sh @ unsw.edu.au")

    parser.add_argument('-a', '--aa-string', help='Single amino acid string', dest='aa_string')
    parser.add_argument('-m', '--msa-dir', help='Directory containing corresponding MSA files for samples', dest='msa_dir')
    parser.add_argument('-d', '--directory', help='Directory containing fasta files', dest='dir')
    parser.add_argument('-p', '--prefix', help='Filename prefix for amino acid strings', dest='aa_prefix', default='manual_entry')
    parser.add_argument('-s', '--suffix', help='Filename suffix for amino acid strings', dest='aa_suffix', default='af2')
    parser.add_argument('-u', '--delim', help='Delimiter in between fields of the amino acid string filename', dest='delim', default='-')
    parser.add_argument('-c', '--seq-chars', help='Number of characters used from the sequence in the filename', dest='seq_chars', default=6)
    parser.add_argument('-o', '--output-file', help='Samplesheet filename', dest='output_file', default='samplesheet.csv')
    parser.add_argument('-x', '--output-extension', help='Extension for string input', default='fasta', dest='output_extension')
    parser.add_argument('-e', '--extension', help='Extension of the files contained in the directory', default='fasta', dest='extension')
    parser.add_argument('-q', '--sequence-header', help='Column name for sequence', default='id', dest='seq_header')
    parser.add_argument('-f', '--fasta-header', help='Column name for fasta path', default='fasta', dest='fasta_header')
    parser.add_argument('-j', '--json', help='Output json format instead of csv', action='store_true', dest='json')
    parser.add_argument('-y', '--yaml', help='Output yaml format instead of csv', action='store_true', dest='yaml')
    parser.add_argument('--yaml-rfaa', help='Output yaml format for RFAA', action='store_true', dest='yaml_rfaa')
    parser.add_argument('-t', '--fasta-dir', help='Output directory for temporary fasta files', default=os.getcwd(), dest='fasta_dir')
    parser.add_argument('-r', '--fasta-match', help='Regex to match for fasta files in directory mode', default='.*\.(fa(a)?(sta)?|y(a)?ml).*$', dest='fasta_regex')
    parser.add_argument('--monomer', help='Create a samplesheet entry for each sample in a fasta file', default=False, action='store_true', dest='monomer')
    parser.add_argument('--version', help='Show version number', default=False, action='store_true', dest='version')
    parser.add_argument('--debug', help='Show debug output', default=False, action='store_true', dest='debug')

    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if (args.version):
        version()
        exit(0)

    if (args.debug):
        version()

    # Validate that an input was provided
    if (not args.aa_string and not args.dir):
        raise ValueError("You must specify an amino acid string or a directory")

    # Validate that seq_chars is an int
    if (type(args.seq_chars) is not int):
        raise ValueError("seq_chars is not a number")

    if (sum([args.json, args.yaml, args.yaml_rfaa]) > 1):
        raise ValueError("Invaid mode combination. You cannot set --json, --yaml and --yaml-rfaa at the same time")

    # Mode
    mode = 0
    mode |= bool(args.dir)
    mode |= args.json << 1
    mode |= args.yaml << 2
    mode |= args.yaml_rfaa << 3
    logger.debug(f"mode: {mode}")
    logger.debug("Will attempt to locate MSAs" if args.msa_dir else "Will NOT attempt to locate MSAs")

    if mode == MODE_STRING_CSV:
        # Generate metadata for AA string
        aa_sample_name = sample_name("".join(args.aa_string.strip().split()), seq_chars=args.seq_chars)
        aa_sample_file_name = file_name(aa_sample_name, prefix=args.aa_prefix, suffix=args.aa_suffix, extension=args.output_extension)
        aa_path = args.fasta_dir + "/" + aa_sample_file_name

        # Create the fasta file
        sample_data = Sample(aa_sample_name, aa_path, "".join(args.aa_string.strip().split()))
        make_fasta(sample_data)

        # Write the samplesheet
        samplesheet_path = args.output_file
        with open(samplesheet_path, "w") as ss_fp:
            create_csv([sample_data], args.seq_header, args.fasta_header, ss_fp)

    if mode == MODE_STRING_JSON:
        # Generate metadata for AA string
        aa_sample_name = sample_name("".join(args.aa_string.strip().split()), seq_chars=args.seq_chars)
        aa_sample_file_name = file_name(aa_sample_name, prefix=args.aa_prefix, suffix=args.aa_suffix, extension=args.output_extension)
        aa_path = args.fasta_dir + "/" + aa_sample_file_name

        # Create the fasta file
        sample_data = Sample(aa_sample_name, aa_path, "".join(args.aa_string.strip().split()))
        make_fasta(sample_data)

        if args.output_file == "samplesheet.csv":
            args.output_file = args.output_file.replace(".csv", ".json")
        samplesheet_path = args.output_file

        with open(samplesheet_path, "w") as ss_fp:
            create_json([sample_data], ss_fp)

    if mode == MODE_STRING_YAML:
        # Generate metadata for AA string
        aa_sample_name = sample_name("".join(args.aa_string.strip().split()), seq_chars=args.seq_chars)
        aa_sample_file_name = file_name(aa_sample_name, prefix=args.aa_prefix, suffix=args.aa_suffix, extension=args.output_extension)
        aa_path = args.fasta_dir + "/" + aa_sample_file_name

        # Create the fasta file
        sample_data = Sample(aa_sample_name, aa_path, "".join(args.aa_string.strip().split()))
        make_fasta(sample_data)

        if args.output_file == "samplesheet.csv":
            args.output_file = args.output_file.replace(".csv", ".yaml")
        samplesheet_path = args.output_file

        with open(samplesheet_path, "w") as ss_fp:
            create_yaml_boltz([sample_data], ss_fp)


    if mode == MODE_DIR_CSV:
        logger.debug(f"Checking {args.dir} for fasta files")
        file_list = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if os.path.isfile(os.path.join(args.dir, f))]
        logger.debug(f"Fasta files: {file_list}")
        file_list = [i for i in file_list if re.search(args.fasta_regex, i)]
        logger.debug(f"File list aginst regex: {file_list}")
        sample_data = []

        samplesheet_path = args.output_file

        for i_file_name in file_list:
            with open(i_file_name, "r") as fp:
                sample_data.append(Sample(os.path.splitext(os.path.basename(fp.name))[0], fp.name, ""))
                logger.debug(f"Added sample {i_file_name}, {sample_data[-1]}")

        samplesheet_path = args.output_file
        logger.debug(f"Sample data array length: {len(sample_data)}")
        with open(samplesheet_path, "w") as ss_fp:
            create_csv(sample_data, args.seq_header, args.fasta_header, ss_fp)

    if mode == MODE_DIR_JSON:
        file_list = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if os.path.isfile(os.path.join(args.dir, f)) and re.search(args.fasta_regex, f)]
        sample_data = []

        for i_file_name in file_list:
            with open(i_file_name, "r") as file_fp:
                sample_data.extend(read_fasta(file_fp, read_data=True, single_line=False))

        samplesheet_path = args.output_file

    if mode == MODE_DIR_YAML:
        logger.debug(f"Checking {args.dir} for fasta files")
        file_list = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if os.path.isfile(os.path.join(args.dir, f))]
        logger.debug(f"Fasta files: {file_list}")
        file_list = [i for i in file_list if re.search(args.fasta_regex, i)]
        logger.debug(f"File list aginst regex: {file_list}")
        sample_data = []

        for i_file_name in file_list:
            with open(i_file_name, "r") as fp:
                fasta_data = read_fasta(fp, read_data=True, single_line=False)
                # Attempt to find MSA if the MSA directory flag is set
                if args.msa_dir:
                    logger.debug(f"Searching for MSAs of {i_file_name}")
                    for fsi, i in zip(fasta_data, range(len(fasta_data))):
                        logger.debug("Checking for " + os.path.join(args.msa_dir, f"{fsi.name}.m3a"))
                        if os.path.isfile(os.path.join(args.msa_dir, f"{fsi.name}.m3a")):
                                fasta_data[i].msa = os.path.join(args.msa_dir, f"{fsi.name}.m3a")
                                logger.debug(f"Added pre-computed MSA for sample {fsi.name} of {i_file_name}: {fsi.msa}")
                        else:
                            logger.debug(f"Corresponding MSA for sample {fsi.name} of {i_file_name} was not found, despite --msa-dir being set. Expected file name is {fsi.name}.m3a. Continuing with no MSA...") 
                sample_data.extend(fasta_data)
                logger.debug(f"Added sample {i_file_name}, {fasta_data}")
                logger.debug(f"Sample data {sample_data[-1].data}")

        if args.output_file == "samplesheet.csv":
            args.output_file = args.output_file.replace(".csv", ".yaml")
        samplesheet_path = args.output_file

        samplesheet_path = args.output_file
        with open(samplesheet_path, "w") as ss_fp:
            create_yaml_boltz(sample_data, ss_fp)

    if mode == MODE_STRING_YAML_RFAA:
        aa_sample_name = sample_name("".join(args.aa_string.strip().split()), seq_chars=args.seq_chars)
        # overwrite defaults
        aa_sample_file_name = file_name(aa_sample_name, prefix=args.aa_prefix, suffix=args.aa_suffix, extension="yaml")
        aa_path = args.fasta_dir + "/" + aa_sample_file_name

        # Create the fasta file
        sample_data = Sample(aa_sample_name, aa_path, "".join(args.aa_string.strip().split()))
        with open(aa_sample_file_name, "w") as s_fp:
            create_yaml_rfaa(sample_data, s_fp)

        samplesheet_path = args.output_file

        with open(samplesheet_path, "w") as ss_fp:
            create_csv([sample_data], args.seq_header, args.fasta_header, ss_fp)
    if mode == MODE_DIR_YAML_RFAA:
        logger.debug(f"Checking {args.dir} for fasta files")
        file_list = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if os.path.isfile(os.path.join(args.dir, f))]
        logger.debug(f"Fasta files: {file_list}")
        file_list = [i for i in file_list if re.search(args.fasta_regex, i)]
        logger.debug(f"File list aginst regex: {file_list}")
        sample_data = []
        
        for i_file_name in file_list:
            with open(i_file_name, "r") as fp:
                fasta_data = read_fasta(fp, read_data=True, single_line=False)
                for i in range(len(fasta_data)):
                    fasta_data[i].path = file_name(sanitize_input(fasta_data[i].name), prefix=args.aa_prefix, suffix=args.aa_suffix, extension="yaml")
                # Attempt to find MSA if the MSA directory flag is set
                sample_data.extend(fasta_data)
                logger.debug(f"Added sample {i_file_name}, {fasta_data}")
                logger.debug(f"Sample data {sample_data[-1].data}")

        for sample in sample_data:
            with open(sample.path, "w") as s_fp:
                create_yaml_rfaa(sample, s_fp)
        
        with open(args.output_file, "w") as ss_fp:
            create_csv(sample_data, args.seq_header, args.fasta_header, ss_fp)
