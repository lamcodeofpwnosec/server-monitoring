rule WebshellDetection
{
    strings:
        $a = "<form" nocase
        $b = "base64_decode" nocase
        $c = "<?php" nocase

    condition:
        $a and $b and $c
}
