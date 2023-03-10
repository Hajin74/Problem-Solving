class BookSolution:
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 0으로 초기화하여 생성
    d = [[0] * m for _ in range(n)]
    
    x, y, direction = map(int, input().split())
    d[x][y] = 1 # 현재 좌표 방문 처리

    # 전체 맵 정보 입력
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    # 방향 정의 (북, 동, 남, 서)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 왼쪽으로 회전
    def turn_left():
        direction -= 1
        if direction == -1 :
            direction = 3
        
    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        turn_left()

        nx = x + dx[direction]
        ny = y + dy[direction]

        # 가보지 않았고 육지인 경우 이동
        if d[nx][ny] == 0 and arr[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 가보았거나 바다인 경우
        else:
            turn_time += 1

            # 네 방향 모두 갈 수 없는 경우
            if turn_time == 4:
                nx = x - dx[direction]
                ny = y - dy[direction]

                # 뒤로 갈 수 있다면 이동하기
                if arr[nx][ny] == 0:
                    x = nx
                    y = nx
                else:
                    break

                turn_time = 9

    print(count)