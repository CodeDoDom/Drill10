# 게임월드 모듈

# 게임월드 표현
world = [[], []]  # world 안에 layer가 담겨 있고, layer 안에 object가 담겨있다.


# 게임월드에 객체 담기
def add_object(o, depth=0):
    world[depth].append(o)  # 지저된 깊이의 레이어에 객체 추가


# 게임월드 객체들을 전부 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()


# 게임 월드의 객체들을 전부 그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()


# 객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('왜 존재하지 않는 걸 지우라고 하지?')
