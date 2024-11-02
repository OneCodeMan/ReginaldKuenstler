//
//  DescriptiveProgressView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-30.
//

import SwiftUI

struct DescriptiveProgressView: View {
    @State var showGridLoading: Bool = false
    @State var message: String = "Loading..."
    var body: some View {
        VStack {
            if showGridLoading {
                GridAnimationView()
            } else {
                VStack {
                    Spacer()
                    ProgressView() {
                        Text(String(localized: "\(message)..."))
                            .font(.defaultFontTitle)
                    }
                    .progressViewStyle(.circular)
                    Spacer()
                }
            }
        }
        .onAppear {
            DispatchQueue.main.asyncAfter(deadline: .now() + 1.2) {
                withAnimation {
                    showGridLoading.toggle()
                }
            }
        }
    }
}

#Preview {
    DescriptiveProgressView()
}
