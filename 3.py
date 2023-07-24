import pandas as pd
import matplotlib.pylab as plt


# 国家
df = pd.read_csv('ISSTA23.csv')
plt.figure(figsize=(10, 6))
country_counts = df['国家'].value_counts()
country_counts.plot(kind='barh')
plt.xlabel('Count')
plt.ylabel('Country')
plt.title('Publication Count by Country')
plt.savefig('Publication Count by Country.jpg')
# print(country_counts)

# 单位
plt.figure(figsize=(10, 8))
affiliation_counts = df['单位'].value_counts()
affiliation_counts[affiliation_counts > 1].plot(kind='bar')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.title('Publication Count by Affiliation')
# plt.savefig('Publication Count by Affiliation.jpg')
# print(affiliation_counts[affiliation_counts > 1])

# 一作
plt.figure(figsize=(10, 8))
affiliation_counts = df['一作'].value_counts()
# affiliation_counts[affiliation_counts > 1].plot(kind='bar')
# plt.xlabel('Count')
# plt.ylabel('Affiliation')
# plt.title('Publication Count by Affiliation')
# plt.savefig('Publication Count by Affiliation.jpg')
print(affiliation_counts[affiliation_counts > 1])

# 作者
author_li = []
df['author'] = df['作者'].apply(lambda x: x.split(', '))
# print(df['author'])
for i in range(df.shape[0]):
    author_li.extend(df.loc[i, 'author'])
# print(author_li)
print('作者总数量', len(author_li))
print('平均每篇论文作者数量：', len(author_li) / df.shape[0])
author_counts = pd.DataFrame(author_li).value_counts()
print(author_counts[author_counts > 2])
