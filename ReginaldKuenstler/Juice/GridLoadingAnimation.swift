import SwiftUI

struct GridAnimationView: View {
    
    @State private var animate: Bool = false
    @State private var color: Color = .gray
    @State private var pattern: [[Int]] = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8,],
        [9, 10, 11, 12, 13, 14, 15, 16, 17,],
        [18, 19, 20, 21, 22, 23, 24, 24, 26,],
        [27, 28, 29, 30, 31, 32, 33, 34, 35,],
        [36, 37, 38, 39, 40, 41, 42, 43, 44,],
        [45, 46, 47, 48, 49, 50, 51, 52, 53,],
        [54, 55, 56, 57, 58, 59, 60, 61, 62,],
        [63, 64, 65, 66, 67, 68, 69, 70, 71,],
        [72, 73, 74, 75, 76, 77, 78, 79, 80,],
    ]

    let colors: [Color] = [.blue, .green, .yellow, .orange]
    
    var body: some View {
        VStack(spacing: 2) {
            ForEach(0..<9) { i in
                HStack(spacing: 2) {
                    ForEach(0..<9) { j in
                        RoundedRectangle(cornerRadius: 12)
                            .foregroundStyle(color)
                            .aspectRatio(1, contentMode: .fit)
                            .scaleEffect(animate ? 1 : 0)
                            .opacity(animate ? 1 : 0)
                            .rotationEffect(.degrees(animate ? 360 : 0))
                            .animation(.easeInOut(duration: 0.1).delay(delay(row: i, col: j)), value: animate)
                    }
                }
            }
        }
        .padding()
        .onAppear {
            // Trigger initial animation immediately
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                animate.toggle()
            }

            Timer.scheduledTimer(withTimeInterval: 1.5, repeats: true) { _ in
                if !animate { color = colors.randomElement()! }
                animate.toggle()
            }
        }
    }
    
    func delay(row: Int, col: Int) -> Double {
        if !pattern.isEmpty {
            let delay = pattern[row][col]
            return Double(delay) * (1.0 / 80.0)
        }
        return 0.0
    }
}
