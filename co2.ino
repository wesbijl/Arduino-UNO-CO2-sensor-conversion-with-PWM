unsigned long pulse_high;  // Time in milliseconds the signal is HIGH
unsigned long period = 1005; // Total cycle time in milliseconds
float Cppm;  // CO2 concentration

void setup() {
  Serial.begin(9600);  
  pinMode(PD3, INPUT);  // Pin 2 is where the PWM signal is connected
}

void loop() {
  pulse_high = pulseIn(PD3, HIGH);  // Measure the time in microseconds the signal is HIGH
  // Convert to milliseconds
  pulse_high = pulse_high / 1000;
  //Serial.println(pulse_high);

  // Calculate CO2 concentration using the provided formula
  if (period > 4) {
    Cppm = 2000.0 * (pulse_high - 2) / (period - 4);
  }

  // Print the concentration
  Serial.print("CO2 concentration: ");
  Serial.print(Cppm);
  Serial.println(" ppm");

  delay(1000);  // Wait for 1 second before the next reading
}
