import os
import folder_paths

class TextDownloader:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {}),
                "filename": ("STRING", {"default": "output.txt"})
            }
        }
    
    RETURN_TYPES = ()
    FUNCTION = "save_text"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def save_text(self, text, filename):
        # 确保文件名有.txt后缀
        if not filename.endswith('.txt'):
            filename += '.txt'
            
        # 构建完整的文件路径
        file_path = os.path.join(self.output_dir, filename)
        
        # 写入文本文件
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Text saved to: {file_path}")
        except Exception as e:
            print(f"Error saving text: {str(e)}")
            
        return {}

NODE_CLASS_MAPPINGS = {
    "TextDownloader": TextDownloader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextDownloader": "Text Downloader"
}