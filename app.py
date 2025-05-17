import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Carregando o dataset com o seaborn

iris_df = sns.load_dataset('iris')

# 2. Análise inicial

print("\nFirst lines:")
print(iris_df.head())

# 3. Tratando os dados ausentes

print("\nMissing values by column:")
print(iris_df.isnull().sum())


# 4. Identificando e tratando outliers

# Criando boxplot
def generator_box_plot(df, columns, ref=""):
    for column in columns:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[column])
        plt.title(f"Boxplot: {column}")
        plt.savefig(f"graphics/{ref}boxplot_{column.replace(' ', '_')}.png")
        plt.close()


generator_box_plot(iris_df, ['petal_length', 'sepal_width'], ref='before_')


# Após identificação dos outliers, utilizarei IQR pelo método interpolado, que é uma forma de identificar outliers
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    filtro = (df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)
    return df[filtro]


# Removendo os outliers e gerando um novo box plot
clean_iris_df = iris_df.copy()
for column in ['petal_length', 'sepal_width']:
    clean_iris_df = remove_outliers(clean_iris_df, column)

generator_box_plot(clean_iris_df, ['petal_length', 'sepal_width'], ref='after_')

# 5. Análise exploratória (EDA)

# Histograma
# É possível ver a relação entre frequencia e os intervalos da largura da sépala
plt.figure(figsize=(6, 4))
sns.histplot(data=clean_iris_df, x='sepal_width', kde=True)
plt.title("Histogram: Sepal Width")
plt.savefig("graphics/hist_sepal_width.png")
plt.close()

# Gráfico de contagem por espécie
# Mostra a frequencia de vezes que cada espécie aparece
plt.figure(figsize=(6, 4))
sns.countplot(data=clean_iris_df, x='species')
plt.title("Count by species")
plt.savefig("graphics/count_species.png")
plt.close()

# Matriz de correlação
# Nota-se algumas correlações fortes entre algumas variáveis que crescem juntas como petal_width e petal_length,
# Também é possível notar correlações fracas como sepal_width e petal_length, sugerindo que a sépalas mais largas,
# tendem a ter pétalas mais curtas
plt.figure(figsize=(8, 6))
sns.heatmap(clean_iris_df.iloc[:, :4].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("graphics/correlation.png")
plt.close()


# 7. Normalizar os dados

# Codificação da variável categórica 'species'
le = LabelEncoder()
clean_iris_df['species'] = le.fit_transform(clean_iris_df['species'])

# Normalizando os dados e a coluna codificada
scaler = StandardScaler()
numeric_column = clean_iris_df.columns
clean_iris_df[numeric_column] = scaler.fit_transform(clean_iris_df[numeric_column])
print("\n", clean_iris_df.head())

# 8. Exportar os dados tratados

clean_iris_df.to_csv("processed_iris.csv", index=False)
print("\nFile 'processed_iris.csv' saved successfully.")
