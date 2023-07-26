import pandas as pd
from fpdf import FPDF

df = pd.read_csv('articles.csv', dtype={'id': str})
print(df)


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df['id'] == self.article_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.article_id, 'price'].squeeze()

    def info_generator(self):
        print(df.loc[df['id'] == self.article_id])
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")


if __name__ == '__main__':
    article_id = input('Choose an article to buy: ')
    df.loc[df['id'] == article_id]['name'].squeeze()
    article = Article(article_id)
    article.info_generator()
