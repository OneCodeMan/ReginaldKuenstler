//
//  OnboardingView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-29.
//

import SwiftUI

struct OnboardingView: View {
    @Binding var hasCompletedOnboarding: Bool
    var body: some View {
        VStack {
            Text("ONBOARDING VIEW")
            Button("Get Started") {
                hasCompletedOnboarding = true
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(8)
        }
    }
}

