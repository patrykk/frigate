import openvino as ov

ov_model = ov.convert_model("/models/ssdlite_mobilenet_v2_coco_2018_05_09/frozen_inference_graph.pb")
for input in ov_model.inputs:
    print(input.get_any_name())


for input in ov_model.inputs:
    print(f"Input name: {input.get_any_name()}")
    print(f"Input partial shape: {input.get_partial_shape()}")
#    print(f"Input layout: {input.get_layout()}")

prep = ov.preprocess.PrePostProcessor(ov_model)
prep.input().tensor().set_layout(ov.Layout("nhwc"))
prep.input().model().set_layout(ov.Layout("nchw"))
prep.input().preprocess().reverse_channels()
ov_model = prep.build()
ov.save_model(ov_model, "/models/ssdlite_mobilenet_v2.xml", compress_to_fp16=True)

