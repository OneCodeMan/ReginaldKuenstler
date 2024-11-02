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
        VStack(alignment: .center) {
            
            Text(String(localized: "Welcome to Pinselton"))
                .font(.defaultFontLargeTitle)
                .fontWeight(.bold)
                .multilineTextAlignment(.center)
            
            Text(String(localized: "Have a great time painting! 😊"))
                .font(.defaultFontCaption)
                .fontWeight(.medium)
                .padding()

            Text(String(localized: "Proceed"))
                .font(.defaultFontButton)
                .frame(maxWidth: .infinity)
                .frame(width: 100, height: 50)
                .background(Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1)))
                .cornerRadius(3)
                .foregroundColor(.white)
                .padding()
                .onTapGesture {
                    hasCompletedOnboarding = true
                }
        }
    }
}

