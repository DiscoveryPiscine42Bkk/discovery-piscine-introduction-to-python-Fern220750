def checkmate(board):
    # แยกกระดานออกเป็นแถว ๆ
    board = board.splitlines()
    n = len(board)
    
    # หาตำแหน่งของพระราชา
    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        print("ข้อผิดพลาด: ไม่พบพระราชาบนกระดาน")
        return
    
    # ทิศทางสำหรับการโจมตีของบิชอป, รู๊ค, และควีน (ทแยง, แนวตั้ง, แนวนอน)
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # ฟังก์ชันตรวจสอบว่าชิ้นส่วนโจมตีพระราชาได้หรือไม่
    def is_in_check_by_piece(piece, directions, range_limit=8):
        for dx, dy in directions:
            x, y = king_pos
            # เคลื่อนไปในทิศทางต่าง ๆ
            for step in range(1, range_limit + 1):
                x += dx
                y += dy
                if 0 <= x < n and 0 <= y < n:
                    # ถ้าช่องว่าง, ให้ไปต่อ
                    if board[x][y] == '.':
                        continue
                    elif board[x][y] == piece:
                        return True
                    else:  # ถ้าชิ้นส่วนอื่นขวางทาง, หยุด
                        break
                else:  # ถ้าหมดขอบกระดาน, หยุด
                    break
        return False
    
    # ตรวจสอบการโจมตีจากเบี้ย (P) (ทแยงเฉียง)
    pawn_attack = False
    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = king_pos[0] + dx, king_pos[1] + dy
        if 0 <= x < n and 0 <= y < n and board[x][y] == 'P':
            pawn_attack = True
            break
    
    # ตรวจสอบการโจมตีจากบิชอป (B) (ทแยง)
    bishop_attack = is_in_check_by_piece('B', bishop_directions)
    
    # ตรวจสอบการโจมตีจากรู๊ค (R) (แนวตั้งและแนวนอน)
    rook_attack = is_in_check_by_piece('R', rook_directions)
    
    # ตรวจสอบการโจมตีจากควีน (Q) (รวมทิศทางของบิชอปและรู๊ค)
    queen_attack = is_in_check_by_piece('Q', bishop_directions + rook_directions)
    
    # ถ้ามีชิ้นส่วนโจมตีพระราชา, พิมพ์ "Success"
    if pawn_attack or bishop_attack or rook_attack or queen_attack:
        print("Success")
    else:
        print("Fail")