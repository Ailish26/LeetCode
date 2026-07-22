class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam_counts = {}

        for user_id, time in logs:
            if user_id not in uam_counts:
                uam_counts[user_id] = set()

            uam_counts[user_id].add(time)

        answer = [0] * k

        for user_id, minutes in uam_counts.items():
            uam = len(minutes)
            answer[uam - 1] += 1

        return answer 