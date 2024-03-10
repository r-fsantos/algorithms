import Foundation
import XCTest

// MARK: - Two Crystal Balls Problem
/// Given two crystal balls that will break if dropped from high enough
/// distance, determine the exact spot in which it will break in the most
/// optimized way.
func twoCrystallBalls(_ breaks: [Bool]) -> Int {
    let step = Int(floor(sqrt(Double(breaks.count))))
    var idx = step

    while (idx < breaks.count) {
        if breaks[idx] {
            break
        }
        idx += step
    }

    idx -= step

    for _ in 0..<min(step, breaks.count) {
        if (breaks[idx]) {
            return idx
        }
        idx += 1
    }

    return -1
}

// MARK: - TestClass
final class SolutionTests: XCTestCase {
    static var allTests = [("solution", testSolution)]

    func testSolution() {
        // Generate a random index between 0 and 9999
        let idx = Int(arc4random_uniform(10000))

        // Initialize an array of 10000 elements, all set to false
        var data = Array(repeating: false, count: 10000)


        // Iterate over the array starting from the random index, setting each element to true
        for i in idx..<10000 {
            data[i] = true
        }

        XCTAssertEqual(twoCrystallBalls(data), idx)
    }
}

SolutionTests.defaultTestSuite.run()
