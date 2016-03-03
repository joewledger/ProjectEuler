package Utils

class PrimeUtils {
  def getPrimeStream () : Stream[Int] = {

    lazy val ps: Stream[Int] = 2 #:: Stream.from(3).filter(i =>
      ps.takeWhile{j => j * j <= i}.forall{ k => i % k > 0});
    return ps;
  }
}
