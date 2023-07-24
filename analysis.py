import os
import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 函数，读取一个文件夹中的所有txt文件
def read_files_in_folder(folder_path):
    file_contents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                file_contents[filename] = file.read()
    return file_contents


# 使用定义的函数读取所有的txt文件
file_contents = read_files_in_folder('abstract')

# 将所有abstract的文本连接到一起
all_abstracts = ' '.join(file_contents.values())
# 创建词云对象
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=nltk.corpus.stopwords.words('english'),
                      min_font_size=10).generate(all_abstracts)
# 展示词云
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('wordcloud_abstract.jpg')
plt.show()

df = pd.read_csv('ISSTA23.csv')
all_titles = ' '.join(df['标题'].tolist())
# 创建词云对象
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=nltk.corpus.stopwords.words('english'),
                      min_font_size=10).generate(all_titles)
# 展示词云
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('wordcloud_title.jpg')
plt.show()



