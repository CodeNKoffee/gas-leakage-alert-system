library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity gas_alert_system is
    port (
        gas_detect_signal : in std_logic;  -- Input from Pico
        buzzer : out std_logic;
        led_alert : out std_logic;
        lcd_display : out std_logic_vector(7 downto 0)
    );
end gas_alert_system;

architecture Behavioral of gas_alert_system is
begin
    process(gas_detect_signal)
    begin
        if gas_detect_signal = '1' then
            buzzer <= '1';
            led_alert <= '1';
            lcd_display <= "X_X";  -- Custom message
        else
            buzzer <= '0';
            led_alert <= '0';
            lcd_display <= "SAFE";  -- Normal state
        end if;
    end process;
end Behavioral;
