    filtered_results = result[result.pred[0][:, 4] > 0.5]

    # 필터링된 결과를 사용하여 객체 정보 얻기
    filtered_boxes = filtered_results.pred[0][:, :4]
    filtered_classes = filtered_results.pred[0][:, 5]

    for bbox, cls in zip(filtered_boxes, filtered_classes):
        x, y, x2, y2 = bbox
        # 이제 x, y, x2, y2 및 cls 변수를 사용하여 필터링된 객체 정보를 처리할 수 있습니다.