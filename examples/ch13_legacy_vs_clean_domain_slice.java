public class MortgageCalc {
    public double WS_PRINCIPAL_AMT = 0.0;
    public double WS_INTEREST_RATE = 0.0;
    public double WS_ACCRUED_INT = 0.0;

    public void calculateInterest() {
        while(true) {
            try {
                double rate = WS_INTEREST_RATE / 1200;
                WS_ACCRUED_INT = WS_PRINCIPAL_AMT * rate;
                break;
            } catch (ArithmeticException e) {
                errorHandler400();
                break;
            }
        }
    }
}
