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
    
    // by doing this here, we populate the map for the entire app cycle
    @StateObject private var colourMapperOG: ColourMapperOG = ColourMapperOG.shared
    @StateObject private var colourCatalog: ColourCatalog = ColourCatalog.shared
    @StateObject private var colourMapper: ColourMapper = ColourMapper.shared
    
    var body: some View {
        if hasCompletedOnboarding {
            ReginaldKuenstlerTabView()
                .environmentObject(userPaletteViewModel) // Your main app view after onboarding is complete
        } else {
            OnboardingView(hasCompletedOnboarding: $hasCompletedOnboarding)
                .environmentObject(userPaletteViewModel)
        }
    }
}

#Preview {
    ContentView()
}
