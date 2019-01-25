import pandas as p
import pandas as p
from Orange.data import Table,Domain
from Orange.evaluation import CrossValidation,scoring
csv_path=("C:\\Users\\acer\\Desktop\\friends\\assg1_room.csv")
data=p.read_csv(csv_path)
#print(data)
te=data['Tenants']

te1=data['Furnished']
mean=te.mean()
te.where(p.notna(te),mean,inplace=True)
te1.where(p.notna(te1),'N/A',inplace=True)
print(te.isnull().values.any())
#print(te)
data['Tenants']=te
print(data['Tenants'].isnull().values.any())
datae1=p.DataFrame(data)
datae1
exportFilePath=("C:\\Users\\acer\\Desktop\\friends\\export.csv")
with open(exportFilePath,"w") as output:
    datae1.to_csv(output,header=True,sep=",")


path1=("C:\\Users\\acer\\Desktop\\friends\\export.csv" )
datae=p.read_csv(path1)

'''
now fro b part'''
from Orange.classification import SklTreeLearner
td=Table.from_file("C:\\Users\\acer\\Desktop\\friends\\export.csv")
#print(data1.domain)
#print(d)
feature_vars=list(td.domain.variables[1:])
class_label_var=td.domain.variables[7]
print(class_label_var)
md=Domain(feature_vars,class_label_var)
#print(d_dis[0])
td=Table.from_table(domain=md,source=td)
#print(.domain.variables[1:])


n1=td.approx_len()
print(n1*80/100)
train_data_set=td[:1360]
test_data_set=td[1360:]
#print(train_data_set.domain)
#print(test_data_set.domain)
tree_learner=SklTreeLearner()
decision_tree=tree_learner(train_data_set)
results=CrossValidation(td,[tree_learner],k=10)
print(decision_tree(test_data_set))
print("Accuracy",scoring.CA(results)[0])
print("AUC",scoring.AUC(results)[0])