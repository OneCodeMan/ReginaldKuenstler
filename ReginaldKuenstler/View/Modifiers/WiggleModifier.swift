/*
 https://gist.github.com/markmals/075273b58a94db20917235fdd5cda3cc
 */

import SwiftUI

extension View {
    func wiggling() -> some View {
        modifier(WiggleModifier())
    }
}

struct WiggleModifier: ViewModifier {
    @State private var isWiggling = false
    
    private static func randomize(interval: TimeInterval, withVariance variance: Double) -> TimeInterval {
        let random = (Double(arc4random_uniform(1000)) - 500.0) / 500.0
        return interval + variance * random
    }
    
    private let rotateAnimation = Animation
        .easeInOut(
            duration: WiggleModifier.randomize(
                interval: 0.14,
                withVariance: 0.025
            )
        )
        .repeatForever(autoreverses: true)
    
    private let bounceAnimation = Animation
        .easeInOut(
            duration: WiggleModifier.randomize(
                interval: 0.18,
                withVariance: 0.025
            )
        )
        .repeatForever(autoreverses: true)
    
    func body(content: Content) -> some View {
        content
            .rotationEffect(.degrees(isWiggling ? 2.0 : 0))
            .animation(rotateAnimation)
            .offset(x: 0, y: isWiggling ? 2.0 : 0)
            .animation(bounceAnimation)
            .onAppear() { isWiggling.toggle() }
    }
}

// Another version
extension View {
    @ViewBuilder
    func jiggle(amount: Double = 3, isEnabled: Bool = true) -> some View {
        if isEnabled {
            modifier(JiggleViewModifier(amount: amount))
        } else {
            self
        }
    }
}

/**
 @State private var isJiggling = false
 Text("🚀")
    .font(.system(size: 84))
    .jiggle(amount: 2, isEnabled: isJiggling)
 */
private struct JiggleViewModifier: ViewModifier {
    let amount: Double

    @State private var isJiggling = false

    func body(content: Content) -> some View {
        content
            .rotationEffect(.degrees(isJiggling ? amount : 0))
            .animation(
                .easeInOut(duration: randomize(interval: 0.14, withVariance: 0.025))
                .repeatForever(autoreverses: true),
                value: isJiggling
            )
            .animation(
                .easeInOut(duration: randomize(interval: 0.18, withVariance: 0.025))
                .repeatForever(autoreverses: true),
                value: isJiggling
            )
            .onAppear {
                isJiggling.toggle()
            }
    }

    private func randomize(interval: TimeInterval, withVariance variance: Double) -> TimeInterval {
         interval + variance * (Double.random(in: 500...1_000) / 500)
    }
}
