'''
paramsで利用できる値たち
https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/deepracer-reward-function-input.html

参考にするとよいかも
https://deepracer-jp.workshop.aws/2_handson/2_2/2_2_6.html
'''

'''
"all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    タイヤが全部trackの上にのっているか。1つでも外れていたらFalse
"x": float,                            # agent's x-coordinate in meters
    トラックを含むシミュレーション環境の x 軸と y 軸に沿ったエージェント中心の位置（メートル単位）。原点は、シミュレーション環境の左下隅
"y": float,                            # agent's y-coordinate in meters
    トラックを含むシミュレーション環境の x 軸と y 軸に沿ったエージェント中心の位置（メートル単位）。原点は、シミュレーション環境の左下隅
"closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    エージェントの現在の位置（x、y）に最も近い 2 つのオブジェクト。
    最初のインデックスは、エージェントの背後にある最も近いオブジェクト。
    2 番目のインデックスは、エージェントの前にある最も近いオブジェクト。
"closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    エージェントの中心からのユークリッド距離によって測定。
    最初の要素はエージェントの背後にある最も近いウェイポイント。
    2 番目の要素はエージェントの前にある最も近いウェイポイント。
"distance_from_center": float,         # distance in meters from the track center 
    エージェントの中心とトラックの中心との間のメートル単位の変位
"is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    エージェントが終了ステータスとして別のオブジェクトにクラッシュした
"is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not.
    エージェントがトラックの中心より左側ならTrue。右側ならFalse 
"is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    エージェントが終了ステータスとしてトラック外に出た
"is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    時計回りならTrue、反時計回りならFalse
"heading": float,                      # agent's yaw in degrees
    座標系の x 軸に対するエージェントの進行方向（度単位）
"objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    0 から track_len までのオブジェクトの距離のリスト
"objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    座標系の x 軸に対する object の進行方向(度)のリスト。BOTカーのためのパラメータ。
"objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    ブーリアン型フラグのリスト。オブジェクトがトラックの中心より左側ならTrue。右側ならFalse 
"objects_location": [(float, float),], # list of object locations [(x,y), ...].
    object の位置情報 (x,y) のリスト。BOTカーの場合、時間の経過で変動する。
"objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    トラック上のオブジェクトの速度（メートル/秒）のリスト。静止オブジェクトの場合、速度は0。ボット車両の場合、値はトレーニングで設定した速度
"progress": float,                     # percentage of track completed
    トラック完走の割合
"speed": float,                        # agent's speed in meters per second (m/s)
    エージェントの観測速度（メートル/秒）
"steering_angle": float,               # agent's steering angle in degrees
    エージェントの中心線からの前輪のステアリング角（度単位）
    負の記号 (-) は右。正の (+) 記号は左。
"steps": int,                          # number steps completed
    完了したステップ数
"track_length": float,                 # track length in meters.
    トラックの長さ（メートル単位）
"track_width": float,                  # width of the track
    トラックの幅 (メートル)。
"waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center
    トラックの中心に沿ったマイルストーンの順序付きリスト。各マイルストーンは、(xw,i、yw,i)
'''


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return float(reward)
