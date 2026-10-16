/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        vector<pair<int, int>> events;
        for(Interval event: intervals)
        {
            events.push_back({event.start, 1});
            events.push_back({event.end, -1});
        }
        
        sort(events.begin(), events.end(), []
        (const pair<int, int>& a, const pair<int, int>& b)
        {
            if(a.first == b.first)
            {
                return a.second < b.second;
            }
            return a.first < b.first;
        });
        int active = 0;
        for(pair<int, int> event : events)
        {
            active += event.second;
            if(active > 1)
            {
                return false;
            }
        }
        return true;
    }
};
