from datetime import timedelta

def solution(video_len, pos, op_start, op_end, commands):
    
    def parse_mm_ss(mm_ss: str) -> timedelta:
        minutes, seconds = map(int, mm_ss.split(':'))
        return timedelta(minutes=minutes, seconds=seconds)
    
    def format_mm_ss(td: timedelta) -> str:
        # 총 초를 정수로
        total_sec = int(td.total_seconds())
        # 음수는 0으로 클램프(원하지 않으면 제거하세요)
        if total_sec < 0:
            total_sec = 0

        minutes, seconds = divmod(total_sec, 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    # 리스트 순서대로 pos 위치를 이동하기만 하면 됨
    curr = parse_mm_ss(pos)
    endTime = parse_mm_ss(video_len)
    op_start_time = parse_mm_ss(op_start)
    op_end_time = parse_mm_ss(op_end)
    if op_start_time<=curr<op_end_time:
        curr = op_end_time
            
    for command in commands:
        
        
        if command == "next":
            curr = min(curr+timedelta(seconds=10),endTime)
        elif command == "prev":
            curr = max(curr-timedelta(seconds=10),timedelta(0))
            
        if op_start_time<=curr<op_end_time:
            curr = op_end_time
        
        ans = format_mm_ss(curr)
    return ans