def is_in_check(board):
    n = len(board)  # ขนาดของกระดาน (n x n)
    king_pos = None
    
    # ค้นหาตำแหน่งของราชา
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        print("Error: King not found")
        return
    
    x, y = king_pos
    
    # ทิศทางที่รูค, ราชินี (แนวนอน, แนวตั้ง) และบิชอป, ราชินี (ทแยงมุม)
    directions = [
        (0, 1), (0, -1),  # แนวนอน
        (1, 0), (-1, 0),  # แนวตั้ง
        (1, 1), (1, -1),  # ทแยงมุม
        (-1, 1), (-1, -1) # ทแยงมุมย้อนกลับ
    ]
    
    # ตรวจสอบแต่ละทิศทาง
    for direction in directions:
        i, j = x, y
        while 0 <= i < n and 0 <= j < n:
            i += direction[0]
            j += direction[1]
            
            if 0 <= i < n and 0 <= j < n:
                piece = board[i][j]
                
                # หากพบหมากรุกศัตรูที่สามารถโจมตีราชา
                if piece == 'R' or piece == 'Q':  # รูคหรือราชินี (ในแนวนอนหรือแนวตั้ง)
                    print("Success")
                    return
                elif piece == 'B' or piece == 'Q':  # บิชอปหรือราชินี (ในทแยงมุม)
                    print("Success")
                    return
                elif piece == 'P':  # เบี้ยสามารถโจมตีในทแยงมุม
                    if direction in [(1, 1), (1, -1)] and i > x:  # เบี้ยโจมตีลง
                        print("Success")
                        return
                    elif direction in [(-1, 1), (-1, -1)] and i < x:  # เบี้ยโจมตีขึ้น
                        print("Success")
                        return
                elif piece != '.':
                    # หากพบหมากรุกตัวอื่น (ที่ไม่ใช่ช่องว่าง) บล็อกการเคลื่อนที่
                    break
    
    # หากไม่มีหมากรุกตัวใดสามารถโจมตีราชาได้
    print("Fail")

# ตัวอย่างการทดสอบ
board = [
    ['.', 'K', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'R', '.', '.', '.', '.'],
    ['.', '.', 'P', '.', 'P', '.', '.', '.'],
    ['.', 'P', '.', 'B', '.', 'B', 'P', '.'],
    ['.', '.', '.', '.', 'B', '.', 'P', '.'],
    ['.', '.', 'P', '.', 'Q', 'P', '.', '.'],
    ['.', '.', '.', 'P', 'P', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.']
]

# ทดสอบฟังก์ชัน
is_in_check(board)
