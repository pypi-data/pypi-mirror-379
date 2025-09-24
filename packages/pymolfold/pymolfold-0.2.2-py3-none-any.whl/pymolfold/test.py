from pxmeter.eval import evaluate

ref_cif = "/home/yifan/other_proj/PymolFold/pymolfold/example/7rss.cif"
model_cif = "/home/yifan/other_proj/PymolFold/pymolfold/example/7rss_protenix_pred.cif"
metric_result = evaluate(
    ref_cif=ref_cif,
    model_cif=model_cif,
)

json_dict = metric_result.to_json_dict()
print(json_dict)