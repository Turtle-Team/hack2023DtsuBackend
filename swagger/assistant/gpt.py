import g4f

class GPTAssitant:
    def __init__(self):
        g4f.logging = True # enable logging
        g4f.check_version = False # Disable automatic version checking
        self.PROMT = 'Ты являешься консультантом для детей в возрасте примерно шести лет по вопросам банковской и экономической граммотности. Все вопросы к тебе будут адресованы внутри тэга <quest></quest>. Если вопрос не отностися к банковской или экономической сфере, отвечай что с данным вопросом "Лучше обратитесь к взрослым с данным вопросом". Отвечай всегда максимально коротко и просто. '

    def send_quest(self, quest: str):
        gpt_quest = f"<quest>{quest}</quest>"
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo_16k,
            messages=[{"role": "user", "content": self.PROMT + gpt_quest}],
        )  # alternative model setting
        return response

    def create_audio_file(self, text_to_speach: str) -> bytes or bytearray:
        pass