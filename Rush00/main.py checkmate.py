def checkmate(board):
    # แปลงกระดานเป็นกริด 2D
    rows = board.splitlines()
    n = len(rows)
    
    # หาตำแหน่งของราชา (King)
    king_pos = None
    for i in range(n):
        for j in range(n):
            if rows[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        return  # ถ้าไม่พบราชา,ออกจากฟังก์ชัน
    
    king_x, king_y = king_pos
    
    #  ทิศทางการเคลื่อนที่ของชิ้นหมากแต่ละตัว
    directions_rook = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #แนวตั้งและแนวนอน
    directions_bishop = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  #ทแยง
    directions_queen = directions_rook + directions_bishop  #ราชินีรวมทักษะของป้อมและบิชอป
    directions_pawn = [(-1, -1), (-1, 1)]  #เบี้ยโจมตีแบบทแยง
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n
    
    # ตรวจสอบว่าชิ้นหมากฝ่ายศัตรูสามารถโจมตีราชาได้หรือไม่
    for i in range(n):
        for j in range(n):
            piece = rows[i][j]
            if piece == '.':
                continue  # ข้ามช่องว่างที่ว่างเปล่า

            if piece == 'P':  # ตรวจสอบเบี้ย
                #เบี้ยสามารถโจมตีได้เฉพาะในทิศทางทแยง ดังนั้นเราต้องตรวจสอบว่าเบี้ยสามารถโจมตีราชาได้หรือไม่
                for dx, dy in directions_pawn:
                    if is_valid(i + dx, j + dy) and i + dx == king_x and j + dy == king_y:
                        print("Success")
                        return
            elif piece == 'R':  # ตรวจสอบป้อม
                for dx, dy in directions_rook:
                    x, y = i, j
                    while is_valid(x + dx, y + dy):
                        x, y = x + dx, y + dy
                        if x == king_x and y == king_y:
                            print("Success")
                            return
                        if rows[x][y] != '.':
                            break  # หยุดถ้าพบชิ้นหมากอื่น ๆ ขวางทาง
            elif piece == 'B':  # ตรวจสอบบิชอป
                for dx, dy in directions_bishop:
                    x, y = i, j
                    while is_valid(x + dx, y + dy):
                        x, y = x + dx, y + dy
                        if x == king_x and y == king_y:
                            print("Success")
                            return
                        if rows[x][y] != '.':
                            break  # หยุดถ้าพบชิ้นหมากอื่น ๆ ขวางทาง
            elif piece == 'Q':  # ตรวจสอบราชินี
                for dx, dy in directions_queen:
                    x, y = i, j
                    while is_valid(x + dx, y + dy):
                        x, y = x + dx, y + dy
                        if x == king_x and y == king_y:
                            print("Success") #ถ้าเกิดการโจมตี
                            return
                        if rows[x][y] != '.':
                            break  # หยุดถ้าพบชิ้นหมากอื่น ๆ ขวางทาง
    #ถ้าไม่พบการโจมตีใดๆ
    print("Fail")
    

def main():
    board = """\
..K.....
...R....
........
....Q...
........
........
........
........\
"""
    checkmate(board)

if __name__ == "__main__":
    main()