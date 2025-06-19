from checkmate import checkmate

def main():
    # ตัวอย่างกระดานหมากรุก
    board = """
    \
        R.......
        .K......
        ..P.....
        .....P..
        R.......
        .B......
        ..P.....
        .....Q..
    \
"""
    checkmate(board)  # เรียกใช้ฟังก์ชัน checkmate จาก checkmate.py

if __name__ == "__main__":
    main()