import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main18891 {
    // 21대 국회의원 선거

    // 비례대표 의석 수 산정 로직

    // 1. 연동 배분 의석 수 ( 총 30석 )
    // 국회의원정수 300 석에서 의석할당정당이 아닌 정당의 당선인 수 + 무소속 당선인 수 를 뺀 후
    // 해당 정당이 얻은 투표비율만큼 곱한 후 해당 정당의 당선인 수를 뺀다.
    // 그 수의 50%에 이를 때까지 의석 수를 우선 할당한다.

    // 2. 조정된 비례대표 의석 수 ( 엳동 배분 의석 수 가 30석이 안된 경우 )
    //
    public static class Party{
        private int index;
        private String partyName;
        private int numOfSeats;
        private int additionalSeats;
        private int additionalSeats2;
        private int numOfVoted;
        private float rateOfVoted;
        private float rates;

        public Party(int index, String partyName, int numOfSeats, int numOfVoted) {
            this.index = index;
            this.partyName = partyName;
            this.numOfSeats = numOfSeats;
            this.numOfVoted = numOfVoted;
        }
        public int getIndex(){
            return index;
        }
        public String getPartyName() {
            return partyName;
        }
        public int getNumOfSeats(){
            return numOfSeats;
        }
        public int getAdditionalSeats() {
            return additionalSeats;
        }
        public void setAdditionalSeats(int seats){
            this.additionalSeats = seats;
        }
        public int getAdditionalSeats2() {
            return additionalSeats2;
        }
        public void setAdditionalSeats2(int seats){
            this.additionalSeats2 = seats;
        }
        public void setNumOfSeats(int numOfSeats) {
            this.numOfSeats = numOfSeats;
        }
        public int getNumOfVoted(){
            return numOfVoted;
        }
        public float getRateOfVoted() {
            return rateOfVoted;
        }
        public void setRateOfVoted(float rate) {
            this.rateOfVoted = rate;
        }
        public float getRates() {
            return rates;
        }
        public void setRates(float rate) {
            this.rates = rate;
        }
    }
    // 정당의 수 P
    private static int P;
    // 총 투표자 수 V
    private static int V;
    // 유효 투표 수 V1
    private static int V1;
    // 의석할당정당 투표받은 수 V2
    private static int V2;
    // 전체의석수 - (의석 할당 정당이 아닌 정당의 지역구 당선인 수 + 무소속 당선인 수) R
    private static int R;
    // 정당이 있는 당선인 수
    private static int E;
    // 무소속 당선인 수
    private static int M;
    // 의석 할당 정당이 아닌 지역구 당선인 수
    private static int N;
    // 정당 리스트
    private static List<Party> parties = new ArrayList<>();
    // 의석을 받을 수 있는 정당들
    private static List<Party> validParties = new ArrayList<>();
    private static List<Party> partiesWithSeats = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        // 입력 값 받아오기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        P = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        for (int i=1; i < P+1; i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int seats = Integer.parseInt(st.nextToken());
            int voted = Integer.parseInt(st.nextToken());
            V1 += voted;
            parties.add(new Party(i, name, seats, voted));
            E += seats;
//            System.out.println(seats + " " + voted);
        }
        // 무소속 당선인 수
        M = 253 - E;
        for (Party party : parties) {
            float rate = (float) party.getNumOfVoted() / V1;
            party.setRateOfVoted(rate);
            if (party.getNumOfSeats() >= 5 || rate*100 > 3) {
                // 의석할당정당 리스트 요소 추가
                validParties.add(party);
                V2 += party.getNumOfVoted();

            } else {
                N += party.numOfSeats;
            }
        }
        // R 값 초기화
        R = M + N;

        // 1. 연동 배분 의석 수 산정
        int totalAddSeats = 0;
        for (Party party : validParties) {
//            System.out.println(party);
            float rate = (float) party.getNumOfVoted() / V2;
            party.setRates(rate);
//            System.out.println(R);
            float tmpSeats = ((300.0f - R) * rate - party.getNumOfSeats()) / 2;
            int additionalSeats;
            if (tmpSeats < 1) additionalSeats = 0;
            else {
                partiesWithSeats.add(party);
                additionalSeats = Math.round(tmpSeats);
                totalAddSeats += additionalSeats;
            }
            party.setAdditionalSeats(additionalSeats);
//            System.out.println(tmpSeats);
        }

        // 2. 좌석 수 검사
        if (totalAddSeats > 30){

        } else if (totalAddSeats < 30){

        }

        // 3. 연동 배분 의석 수 조정
        // 4. 나머지 17석에 대해 의석 배분
        // 5. 의석 수 많은 순, 같다면 사전순으로 정당명이 우선인 순
    }
}
