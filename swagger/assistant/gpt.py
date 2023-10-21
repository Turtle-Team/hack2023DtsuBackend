import g4f

class GPTAssitant:
    def __init__(self):
        g4f.logging = True # enable logging
        g4f.check_version = False # Disable automatic version checking
        self.PROMT = 'Тебя зовут Тортила. Ты являешься консультантом для детей в возрасте примерно шести лет по вопросам банковской и экономической граммотности. Все вопросы к тебе будут адресованы внутри тэга <quest></quest>. Если вопрос не отностися к банковской или экономической сфере, отвечай что с данным вопросом "Лучше обратитесь к взрослым с данным вопросом". Отвечай всегда максимально коротко и просто. Отвечай всегда на русском языке. Не пиши на китайском, японском и иных языках кроме русского языка. Русский язык это твой основной язык. "流量异常" переводи как "Лучше обратись к взрослым".'


    def send_quest(self, quest: str):
        gpt_quest = f"<quest>{quest}</quest>"
        response = g4f.ChatCompletion.create(
        model=g4f.models.default,

        messages=[{"role": "user", "content": self.PROMT + gpt_quest}],
        return response

    def create_audio_file(self, text_to_speach: str) -> bytes or bytearray:
        pass