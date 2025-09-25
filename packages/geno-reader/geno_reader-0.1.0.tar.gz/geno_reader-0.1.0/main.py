from geno_reader import GenoReader

def main():
    reader = GenoReader(plink_suffix="test_data/penncath_sorted_bed", chunk_size=2048)
    counts = 0
    for item in reader:
        print(item.sample_id)
        print(item.genotypes_as_numpy())
        counts += 1

    print(f"COUNTS: {counts}")





if __name__ == "__main__":
    main()
