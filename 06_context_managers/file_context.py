class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file {self.filename}...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  # Propaga la excepción si ocurre
