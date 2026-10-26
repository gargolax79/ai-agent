import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_directory = os.path.abspath(working_directory)
        target_directory = os.path.normpath(
            os.path.join(abs_working_directory, directory)
        )

        # True or False if the target directory is a subdirectory of the working directory
        valid_target_directory = (
            os.path.commonpath([abs_working_directory, target_directory])
            == abs_working_directory
        )

        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory):
            return f'Error: {directory}" is not a directory'

        files_info = []
        for item in os.listdir(target_directory):
            item_name = item
            item_size = os.path.getsize(os.path.join(target_directory, item))
            item_is_dir = os.path.isdir(os.path.join(target_directory, item))
            files_info.append(
                f"- {item_name}: file_size={item_size} bytes, is_dir={item_is_dir}"
            )

        # return f'Success: "{directory}" is within the working directory'
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
