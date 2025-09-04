import System.CPUTime
import Text.Printf

-- Algoritmo recursivo de Euclides
gcdEuclides :: Integer -> Integer -> Integer
gcdEuclides a 0 = a
gcdEuclides a b = gcdEuclides b (a `mod` b)

main :: IO ()
main = do
    let a = 987654321
        b = 123456789
        repeticiones = 1000000
    inicio <- getCPUTime
    let resultado = foldl (\acc _ -> gcdEuclides a b) 0 [1..repeticiones]
    fin <- getCPUTime
    let tiempo = fromIntegral (fin - inicio) / (10^12) -- segundos
    printf "MCD(%d, %d) = %d\n" a b resultado
    printf "Tiempo en Haskell: %f segundos\n" (tiempo :: Double)
