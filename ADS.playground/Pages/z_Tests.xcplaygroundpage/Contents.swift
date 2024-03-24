import Foundation
import XCTest

// Sources models, helpers, etc
import PlaygroundSupport

final class SolutionTest: XCTestCase {
    static var allCases = [("solution", testSolution)]

    func testSolution() {
        let queue = Queue<Int>()

        (0..<10).forEach { queue.enqueue($0) }

        XCTAssertEqual(queue.length, 10)
        XCTAssertEqual(queue.peek()!, 0)

        XCTAssertEqual(queue.dequeue(), 0)
        XCTAssertEqual(queue.length, 9)
        XCTAssertEqual(queue.peek()!, 1)
    }
}

SolutionTest.defaultTestSuite.run()
