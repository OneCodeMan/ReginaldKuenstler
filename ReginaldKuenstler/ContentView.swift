//
//  ContentView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-15.
//

import SwiftUI

struct ContentView: View {
    @AppStorage("hasCompletedOnboarding") var hasCompletedOnboarding = false
    @EnvironmentObject var userPaletteViewModel: UserPaletteViewModel // Injected from the environment
    var body: some View {
        if hasCompletedOnboarding {
            ReginaldKuenstlerTabView()
                .environmentObject(userPaletteViewModel) // Your main app view after onboarding is complete
        } else {
            OnboardingView(hasCompletedOnboarding: $hasCompletedOnboarding)
        }
    }
}

#Preview {
    ContentView()
}
