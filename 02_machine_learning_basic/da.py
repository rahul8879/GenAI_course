import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
# print(type(df))

# print(df.head(5)). # select * from df limit 5
# print(df.tail(5))

# print(df[['cibil_score','status']].head(10))
# select cibil_score, status from df limit 5
# only one columns
# print(type(df['cibil_score']))
# print(df['cibil_score'].mean())
# print(df['cibil_score'].median())
# print(df['cibil_score'].mode())
# print(df['cibil_score'].min())

# print(df.info())

approved_df = df[df['status'] == 'Approved']
rejected_df = df[df['status'] == 'Rejected']
print(approved_df.head(5))
print(rejected_df.head(5))


# some basic analysis

# I can compare these 2 groups
# avg cibil score for approved customer
print(approved_df['cibil_score'].mean())
# avg cibil score for rejected customer
print(rejected_df['cibil_score'].mean())


# print(df.shape)
# print(df.columns)
# print(df.describe())
# print(df.dtypes)
# print(df.info())

# to plot histoplot
plt.figure(figsize=(10,5))
sns.histplot(approved_df['cibil_score'], kde=False, color='green', label='Approved', bins=30)
sns.histplot(rejected_df['cibil_score'], kde=False, color='red', label='Rejected', bins=30)
plt.legend()
plt.title('Distribution of CIBIL Scores')
plt.xlabel('CIBIL Score')
plt.ylabel('Frequency')
# plt.show()

# save the image
plt.savefig('cibil_score_distribution.png')


# same things we can do for other features - income
# but in income : string --> symbol Rupees//
def clean_income(income_str):
    if isinstance(income_str, str):
        return float(income_str.replace('₹', '').replace(',', '').strip())
    return income_str

df['income'] = df['income'].apply(clean_income)

# for the income also we can do the same kind of analysis

approved_income_df = df[df['status'] == 'Approved']
rejected_income_df = df[df['status'] == 'Rejected']
# print(approved_income_df.head(5))
# print(rejected_income_df.head(5))
# avg income for approved customer
print(approved_income_df['income'].mean())
# avg income for rejected customer
print(rejected_income_df['income'].mean())


# some basic analysis

# I can compare these 2 groups
# avg income for approved customer
print(approved_income_df['income'].mean())
# avg income for rejected customer
print(rejected_income_df['income'].mean())


# to plot histoplot
plt.figure(figsize=(10,5))
sns.histplot(approved_income_df['income'], kde=False, color='green', label='Approved', bins=30)
sns.histplot(rejected_income_df['income'], kde=False, color='red', label='Rejected', bins=30)
plt.legend()
plt.title('Distribution of Income')
plt.xlabel('Income')
plt.ylabel('Frequency')
# plt.show()
plt.savefig('income_distribution.png')


# git fetch main
# git merge origin/main