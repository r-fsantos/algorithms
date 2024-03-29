import Foundation
import XCTest

// MARK: - Implementation
func binarySearch(haystack: [Int], needle: Int) -> Bool {
    var lo = 0
    var hi = haystack.count

    repeat {
        var m = Int( floor( Double( (lo + (hi - lo) / 2) ) ) )

        if haystack[m] == needle {
            return true;
        } else if (haystack[m] > needle) {
            hi = m
        } else {
            lo = m + 1
        }

    } while (lo < hi)

    return false
}

// MARK: - Tests
final class SolutionTests: XCTestCase {
    static var allTests = [("solution", testSolution)]

    func testSolution() {
        let foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        XCTAssertEqual(binarySearch(haystack: foo, needle: 69), true)
        XCTAssertEqual(binarySearch(haystack: foo, needle: 1336), false)
        XCTAssertEqual(binarySearch(haystack: foo, needle: 69420), true)
        XCTAssertEqual(binarySearch(haystack: foo, needle: 69421), false)
        XCTAssertEqual(binarySearch(haystack: foo, needle: 1), true)
        XCTAssertEqual(binarySearch(haystack: foo, needle: 0), false)
    }
}

SolutionTests.defaultTestSuite.run()

