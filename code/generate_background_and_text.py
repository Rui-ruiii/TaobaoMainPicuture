from PIL import Image, ImageDraw, ImageFont
import os,configparser
cf = configparser.ConfigParser()
cf.read("../env/config.ini")

font1 = 'ONYX.TTF'
font2 = 'NIAGENG.TTF'
font3 = 'SIMYOU.TTF'


class ImgText:
    font = ImageFont.truetype(font1, 70)

    def __init__(self, title, title_font_type,title_font_size,title_font_color,content, size, backColor,content_font_type,content_font_size,content_font_color):
        # 预设宽度 可以修改成你需要的图片宽度
        self.width = 1600
        self.size = size
        self.title = title
        self.title_font_type = title_font_type
        self.title_font_size = title_font_size
        self.title_font_color = title_font_color
        self.content = content
        self.backColor = backColor
        self.content_font_type = content_font_type
        self.content_font_size = content_font_size
        self.content_font_color = content_font_color
        # 文本
        # self.text = text
        # 段落 , 行数, 行高
        self.duanluo, self.note_height, self.line_height = self.split_text()

    def get_duanluo(self, text):
        txt = Image.new('RGBA',self.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)
        # 所有文字的段落
        duanluo = ""
        # 宽度总和
        sum_width = 0
        # 几行
        line_count = 1
        # 行高
        line_height = 0
        for char in text:
            width, height = draw.textsize(char, ImageFont.truetype(self.content_font_type, self.content_font_size))
            sum_width += width
            if sum_width > self.width:  # 超过预设宽度就修改段落 以及当前行数
                line_count += 1
                sum_width = 0
                duanluo += '\n'
            duanluo += char
            line_height = max(height, line_height)
        if not duanluo.endswith('\n'):
            duanluo += '\n'
        return duanluo, line_height, line_count

    def split_text(self):
        # 按规定宽度分组
        max_line_height, total_lines = 0, 0
        allText = []
        for text in self.content.split('\n'):
            duanluo, line_height, line_count = self.get_duanluo(self.content)
            max_line_height = max(line_height, max_line_height)
            total_lines += line_count
            allText.append((duanluo, line_count))
        line_height = max_line_height
        total_height = total_lines * line_height
        return allText, total_height, line_height

    def RGB_to_Hex(self, color):
        # rgb = tmp.split(',')  # 将RGB格式划分开来
        # strs = '#'
        # for i in rgb:
        #     num = int(i)  # 将str转int
        #     # 将R、G、B分别转化为16进制拼接转换并大写
        #     strs += str(hex(num))[-2:].replace('x', '0').upper()
        #     # print(strs)
        #     # color = RGB_to_Hex('249,204,190')
        img = Image.new("RGBA", self.size, color)
        img.save("../source_pic/background.png")

    def draw_text(self,title_position,content_position,result_picture):
        self.RGB_to_Hex(self.backColor)
        """
        绘图以及文字
        :return:
        """
        note_img = Image.open('../source_pic/background.png').convert("RGBA")
        draw = ImageDraw.Draw(note_img)

        # header = 'this is a title'
        # font_type = 'ABACE-PFB-2.ttf'
        font_type = self.title_font_type
        font_size = self.title_font_size

        color = "#FFFFFF"
        header_font = ImageFont.truetype(font_type, font_size)

        header_x = 100
        header_y = 100
        print(self.title)
        draw.text(title_position, u'%s' % self.title, fill=self.title_font_color, font=header_font)

        # 左上角开始
        x, y = 100, 300
        for duanluo, line_count in self.duanluo:
            draw.text(content_position, duanluo, fill=self.content_font_color, font=ImageFont.truetype(self.content_font_type, self.content_font_size))
            y += self.line_height * line_count
        # note_img.show()
        note_img.save("../resul_v1" + "/" + result_picture)


def Run(title, title_position,title_font_type,title_font_size,title_font_color,content, content_position,picture_size_5, picture_color,content_font_type,content_font_size,content_font_color,result_picture):
    n = ImgText(title, title_font_type,title_font_size,title_font_color,content, picture_size_5, picture_color,content_font_type,content_font_size,content_font_color)
    n.draw_text(title_position,content_position,result_picture)

def RM_background(background_path):
    os.remove(background_path)

if __name__ == '__main__':

    picture_size_5 = (2208, 1242)
    picture_color = (255, 255, 255)
    result_picture = "backResult1.png"

    title = 'JESSIRO'
    title_position = (750, 400)
    title_font_type = font2
    title_font_color = (0,0,0)
    title_font_size = 400

    content = '优雅  ·  时尚'
    content_position = (850, 900)
    content_font_type = font3
    content_font_color = (0,0,0)
    content_font_size = 80


    Run(title,title_position,title_font_type,title_font_size,title_font_color,content, content_position,picture_size_5, picture_color,content_font_type,content_font_size,content_font_color,result_picture)
    os.remove("../source_pic/background.png")