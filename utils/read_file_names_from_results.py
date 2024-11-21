def read_the_existing_file_names(path: str) -> list:
    with open(path, "r") as f:
        lines = f.readlines()
        f.close()
        return [line.split(";")[0].strip() for line in lines]