# N: 3의 거듭제곱(3, 9, 27, ...), 크기 N의 패턴: N×N 정사각형 모양
def draw_stars(n):
  if n == 1:
    return ['*']

  Stars = draw_stars(n//3)
  L = []

  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)

  return L

N = int(input())
print('\n'.join(draw_stars(N)))  # 리스트에 있는 요소 하나하나 사이에 구분자를 넣어 합쳐서 하나의 문자열로 바꾸어 반환

# N이 3보다 클 경우,
# 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을
# 크기 N/3의 패턴으로 둘러싼 형태