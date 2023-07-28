class FileCreator:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
            print(f"File '{self.filename}' created successfully.")
        except Exception as e:
            print(f"Error creating file '{self.filename}': {str(e)}")
filename = "Sam.txt"
content = "There is a beautiful flower"
creator = FileCreator(filename)
creator.create_file(content)
