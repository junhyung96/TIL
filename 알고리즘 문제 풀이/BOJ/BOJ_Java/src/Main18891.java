import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

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
        private int index; // 정당 기호
        private String partyName; // 정당 이름
        private int numOfSeats; // 지역구 의원 당선 수
        private int additionalSeats; // 연동 배분 비례대표 의원수
        private int additionalSeats2; // 17석 배분 수
        private int numOfVoted; // 투표 받은 수
        private double rateOfVoted; // 투표 받은 비율 (전체)
        private double rates; // 투표 받은 비율 (의석할당전당)
        private double ratesWithOut; // 투표 받은 비율 (의석할당전당, 소수점 아래 값)

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
        public double getRateOfVoted() {
            return rateOfVoted;
        }
        public void setRateOfVoted(double rate) {
            this.rateOfVoted = rate;
        }
        public double getRates() {
            return rates;
        }
        public void setRates(double rate) {
            this.rates = rate;
        }
        public double getRatesWithOut () { return ratesWithOut; }
        public void setRatesWithOut (double ratesWithOut) { this.ratesWithOut = ratesWithOut; }
    }

    private static int P;  // 정당의 수 P
    private static int V; // 총 투표자 수 V
    private static int V1; // 유효 투표 수 V1
    private static int V2; // 의석할당정당 투표받은 수 V2
    private static int R; // 전체의석수 - (의석 할당 정당이 아닌 정당의 지역구 당선인 수 + 무소속 당선인 수) R
    private static int E; // 정당이 있는 당선인 수
    private static int M; // 무소속 당선인 수
    private static int N; // 의석 할당 정당이 아닌 지역구 당선인 수
    // 정당 리스트
    private static List<Party> parties = new ArrayList<>();
    // 의석을 받을 수 있는 정당들
    private static List<Party> validParties = new ArrayList<>();
    // 의석을 배정받은 정당들
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
            double rate = (double) party.getNumOfVoted() / V1;
//            System.out.println(rate);
            party.setRateOfVoted(rate);
            if (party.getNumOfSeats() >= 5 || rate >= 0.03) {
                // 의석할당정당 리스트 요소 추가
                validParties.add(party);
                V2 += party.getNumOfVoted();

            } else {
                N += party.numOfSeats;
            }
        }
        // R 값 초기화
        R = M + N;
//        System.out.println(R + " " + M + " " + N);
        // 1. 연동 배분 의석 수 산정
        int totalAddSeats = 0;
        for (Party party : validParties) {
//            System.out.println(party);
            double rate = (double) party.getNumOfVoted() / V2;
            party.setRates(rate);
//            System.out.println(R);
            double tmpSeats = ((300.0 - R) * rate - party.getNumOfSeats()) / 2;
            int additionalSeats;
            if (tmpSeats < 1) additionalSeats = 0;
            else {
                partiesWithSeats.add(party);
                BigDecimal bd = new BigDecimal(Double.toString(tmpSeats));
                additionalSeats = bd.setScale(0, RoundingMode.HALF_UP).intValue();
                totalAddSeats += additionalSeats;
            }
            party.setAdditionalSeats(additionalSeats);
        }
        // 2. 좌석 수 검사, 연동 배분 의석 수 조정
        if (totalAddSeats > 30){
            // tmpTotal 이 30 이 될 때까지 배분
            int tmpTotal = 0;
            // 정수 부분 배분
            for (Party party : partiesWithSeats) {
                double tmpSeats = 30.0 * party.getAdditionalSeats() / totalAddSeats;
                int tmpSeats2 = (int) Math.floor(tmpSeats);
                party.setAdditionalSeats(tmpSeats2);
                party.setRatesWithOut(tmpSeats - tmpSeats2);
                tmpTotal += tmpSeats2;
            }
            // 소수점 기준 정렬
            Collections.sort(partiesWithSeats, new Comparator<Party>() {
                @Override
                public int compare(Party o1, Party o2) {
                    int numberCompare = Double.compare(o2.ratesWithOut, o1.ratesWithOut);
                    if (numberCompare != 0) {
                        return numberCompare;
                    } else {
                        return Integer.compare(o1.index, o2.index);
                    }
                }
            });
            // 소수점 배분
            for (Party party : partiesWithSeats) {
                if (tmpTotal < 30) {
                    party.setAdditionalSeats(party.getAdditionalSeats() + 1);
                    tmpTotal += 1;
                } else break;
            }
        } else if (totalAddSeats < 30){
            // tmpTotal 이 30 이 될 때까지 배분
            int tmpTotal = 0;
            // 정수 부분 배분
            for (Party party : partiesWithSeats) {
//                System.out.println(party.getRates());
                double tmpSeats = (30.0 - totalAddSeats) * party.getRates();
                int tmpSeats2 = (int) Math.floor(tmpSeats);
//                System.out.println(tmpSeats2);
                party.setAdditionalSeats(party.getAdditionalSeats() + tmpSeats2);
                party.setRatesWithOut(tmpSeats - tmpSeats2);
                tmpTotal += party.getAdditionalSeats() + tmpSeats2;
            }
            // 소수점 기준 정렬
            Collections.sort(partiesWithSeats, new Comparator<Party>() {
                @Override
                public int compare(Party o1, Party o2) {
                    int numberCompare = Double.compare(o2.ratesWithOut, o1.ratesWithOut);
                    if (numberCompare != 0) {
                        return numberCompare;
                    } else {
                        return Integer.compare(o1.index, o2.index);
                    }
                }
            });
            // 소수점 배분
            for (Party party : partiesWithSeats) {
                if (tmpTotal < 30) {
                    party.setAdditionalSeats(party.getAdditionalSeats() + 1);
                    tmpTotal += 1;
                } else break;
            }
        }


        // 4. 나머지 17석에 대해 의석 배분
        // tmpTotal 이 30 이 될 때까지 배분
        int tmp17 = 0;
        // 정수 부분 배분
        for (Party party : validParties) {
            double tmpSeats = 17 * party.getRates();
            int tmpSeats2 = (int) Math.floor(tmpSeats);
//            System.out.println(tmpSeats2);
            party.setAdditionalSeats2(tmpSeats2);
            party.setRatesWithOut(tmpSeats - tmpSeats2);
            tmp17 += tmpSeats2;
        }
        // 소수점 기준 정렬
        Collections.sort(validParties, new Comparator<Party>() {
            @Override
            public int compare(Party o1, Party o2) {
                int numberCompare = Double.compare(o2.ratesWithOut, o1.ratesWithOut);
                if (numberCompare != 0) {
                    return numberCompare;
                } else {
                    return Integer.compare(o1.index, o2.index);
                }
            }
        });
        // 소수점 배분
        for (Party party : validParties) {
            if (tmp17 < 17) {
//                System.out.println(party.getPartyName());
                party.setAdditionalSeats2(party.getAdditionalSeats2() + 1);
                tmp17 += 1;
            } else break;
        }

        for (Party party : parties) {
            party.setNumOfSeats(party.getNumOfSeats() + party.getAdditionalSeats() + party.getAdditionalSeats2());
        }

        // 5. 의석 수 많은 순, 같다면 사전순으로 정당명이 우선인 순
        Collections.sort(parties, new Comparator<Party>() {
            @Override
            public int compare(Party o1, Party o2) {
                if (o1.numOfSeats != o2.numOfSeats){
                    return o2.numOfSeats - o1.numOfSeats;
                } else{
                    return o1.partyName.compareTo(o2.partyName);
                }
            }
        });

        StringBuilder sb = new StringBuilder();
        for (Party party : parties) {
//            System.out.println(party.additionalSeats + " " + party.additionalSeats2);
//            int totalSeat = party.getNumOfSeats() + party.getAdditionalSeats() + party.getAdditionalSeats2();
            sb.append(party.getPartyName() + " " + party.getNumOfSeats());
            sb.append("\n");
        }
        System.out.println(sb);
    }

}
