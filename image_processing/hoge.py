import numpy as np
import cv2
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()  #Dlibに用意されている検出器をセット
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") # 学習済みファイル読み込み
    
while True:
    ret, frame = cap.read()
    height_pre, width_pre, colors = frame.shape
    scale = 3
    height, width = height_pre//scale, width_pre//scale
    if not ret: break
    src = cv2.resize(frame, dsize=(width, height)) # 画像サイズを小さくして処理負担の軽減
    src = cv2.flip(src, flipCode=1) # 左右反転
    
    mosaic_scale = 10
    mosaic = cv2.resize(src, dsize=(width//mosaic_scale, height//mosaic_scale), interpolation=0)
    mosaic = cv2.resize(mosaic, dsize=(width, height), interpolation=0)
    
    dst = src.copy()
    
    faces = detector(src[:, :, ::-1])  #画像中の全てを探索して「顔らしい箇所」を検出
    if len(faces) > 0:  # 顔を見つけたら以下を処理する
        for face in faces:  #全ての顔 faces から一つの face を取り出して
            parts = predictor(src, face).parts()  #顔パーツ推定
            
            # TODO: x座標の最小値・最大値, y座標の最小値・最大値を定義する
            # tips: 変数を4つ作る
            ymin = height
            ymax = 0
            xmin = width
            xmax = 0
            
            for i in parts:
                cv2.circle(src, (i.x, i.y), 1, (0, 255, 0), -1) # 点をプロット
                
                # TODO: x座標の最小値・最大値, y座標の最小値・最大値を吟味する
                if xmin > i.x: xmin = i.x # x最小値の更新
                if xmax < i.x: xmax = i.x
                if ymin > i.y: ymin = i.y
                if ymax < i.y: ymax = i.y
                
            # TODO: x座標の最小値〜最大値, y座標の最小値〜最大値の範囲の部分だけ、
            # モザイク画像にすり替える
            dst[ymin:ymax, xmin:xmax, :] = mosaic[ymin:ymax, xmin:xmax, :]

    
    cv2.imshow("cameraCaptured", src)
    cv2.imshow("cameraCapturedMosaiced", mosaic)
    cv2.imshow("cameraCapturedResult", dst)
    if cv2.waitKey(1) == ord('q'): break
    
cap.release()
cv2.destroyAllWindows()