import json

path = "in_class-activity_4_28.ipynb"
with open(path, "r") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        for i, line in enumerate(source):
            if 'scoring=["accuracy","precision","recall","f1","balanced_accuracy"]' in line:
                source[i] = line.replace('scoring=["accuracy","precision","recall","f1","balanced_accuracy"]', 'scoring=["accuracy","precision_weighted","recall_weighted","f1_weighted","balanced_accuracy"]')
            
            if 'scores["test_precision"]' in line:
                source[i] = line.replace('scores["test_precision"]', 'scores["test_precision_weighted"]')
            if 'scores["test_recall"]' in line:
                source[i] = line.replace('scores["test_recall"]', 'scores["test_recall_weighted"]')
            if 'scores["test_f1"]' in line:
                source[i] = line.replace('scores["test_f1"]', 'scores["test_f1_weighted"]')
                
            if 'precision_score(y_test,preds,zero_division=0)' in line:
                source[i] = line.replace('precision_score(y_test,preds,zero_division=0)', "precision_score(y_test,preds,zero_division=0, average='weighted')")
            if 'recall_score(y_test,preds,zero_division=0)' in line:
                source[i] = line.replace('recall_score(y_test,preds,zero_division=0)', "recall_score(y_test,preds,zero_division=0, average='weighted')")
            if 'f1_score(y_test,preds,zero_division=0)' in line:
                source[i] = line.replace('f1_score(y_test,preds,zero_division=0)', "f1_score(y_test,preds,zero_division=0, average='weighted')")
                
            if 'precision_score(y_true,preds,zero_division=0)' in line:
                source[i] = line.replace('precision_score(y_true,preds,zero_division=0)', "precision_score(y_true,preds,zero_division=0, average='weighted')")
            if 'recall_score(y_true,preds,zero_division=0)' in line:
                source[i] = line.replace('recall_score(y_true,preds,zero_division=0)', "recall_score(y_true,preds,zero_division=0, average='weighted')")
            if 'f1_score(y_true,preds,zero_division=0)' in line:
                source[i] = line.replace('f1_score(y_true,preds,zero_division=0)', "f1_score(y_true,preds,zero_division=0, average='weighted')")

with open(path, "w") as f:
    json.dump(nb, f, indent=1)
print("Notebook patched successfully.")
