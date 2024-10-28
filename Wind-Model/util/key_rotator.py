# File to circumvent API limits by rotating multiple user API keys for requests
from datetime import datetime

class APIKeyRotator:

    class APIKey:
        def __init__(self,key) -> None:
            self.key__ = key
            self.used__ = False

        def __str__(self) -> str:
            if(self.used__):
                raise KeyError("APIKeyRotator exception : Unable to use key (__str__) more than once. Please request a new rotated key with .get_key() !")
            self.used__ = True
            return self.key__

    def get_date_s__(self) -> str:
        return datetime.today().strftime('%Y-%m-%d')

    def __init__(self, rotator_file, api_key_file) -> None:
        self.file__ = rotator_file
        self.key_index__ = 0
        self.date_stamp__ = self.get_date_s__()
        self.used_today__ = 0
        with open(api_key_file, "r") as apk_file:
            file_raw = apk_file.read()
            self.keys__ = file_raw.split("\n")
            self.key_count__ = len(self.keys__)

        self.load_metadata__()


    def generate_meta__(self) -> None:
        with open(self.file__, "w") as meta:
            meta.write(f"using 0\naccesses 0\nlast {self.get_date_s__()}")

    def decode_meta__(meta_str: str):
        current_key = int(meta_str.split("\n")[0].split(" ")[1])
        accesses = int(meta_str.split("\n")[1].split(" ")[1])
        current_ds = meta_str.split("\n")[2].split(" ")[1]

        return current_key, accesses, current_ds
    
    def load_metadata__(self):
        with open(self.file__, "r") as meta:
            meta_raw = meta.read()
            if(meta_raw == "?"):
                self.generate_meta__()
            else:
                self.key_index__, self.used_today__, self.date_stamp__ = APIKeyRotator.decode_meta__(meta_raw)

    def get_key(self) -> APIKey:
        if(self.keys_remaining() <= 0):
            raise KeyError("API rotator cannot provide any more keys (All keys have been used up! Add more into API keys source file)")
        key__: str = self.keys__[self.key_index__]
        self.key_index__ = (self.key_index__+1) % self.key_count__

        # Check if accesses have reset
        with open(self.file__, "r") as meta:
            meta_raw = meta.read()
            index, accesses, ds = APIKeyRotator.decode_meta__(meta_raw)
            cur_ds = self.get_date_s__()
            if(ds != cur_ds):
                # Accesses have reset!
                self.used_today__ = 0
                self.date_stamp__ = cur_ds

        # Update current access values
        self.used_today__ += 1
        with open(self.file__, "w") as meta:
            meta.write(f"using {self.key_index__}\naccesses {self.used_today__}\nlast {self.date_stamp__}")

        return APIKeyRotator.APIKey(key__)

    def keys_remaining(self) -> int:
        return self.key_count__*10 - self.used_today__

            



    



    