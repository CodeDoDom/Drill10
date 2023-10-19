# 게임월드 모듈

# 게임월드 표현
world = []

# 게임월드에 객체 담기
def add_object(o):
    world.append(o)

# 게임월드 객체들을 전부 업데이트
def update():
    for o in world:
        o.update()

# 게임 월드의 객체들을 전부 그리기
def render():
    for o in world:
        o.draw()

# 객체 삭제
def remove_object(o):
    world.remove(o)

