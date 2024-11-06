//
//  ReginaldKuenstlerTabView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

/**
 Two tabs:
 - your palette
 - image generator.
 */

import SwiftUI

struct ReginaldKuenstlerTabView: View {
    @EnvironmentObject var userPaletteViewModel: UserPaletteViewModel // Access the ViewModel

    @State var selectedTab: Int = 3
    var body: some View {
        TabView(selection:  $selectedTab) {
            UserPaletteView()
                .environmentObject(userPaletteViewModel)
                .tag(0)
                .tabItem {
                    Image(systemName: "paintpalette.fill")
                        .renderingMode(.template)
                        .foregroundColor(.red) // <2>
                    Text(String(localized: "Your Palette"))
                }
                .font(.defaultFontCaption)
            
            ColourComparisonView()
                .environmentObject(userPaletteViewModel)
                .tag(1)
                .tabItem {
                    Image(systemName: "chart.bar.fill")
                        .renderingMode(.template)
                    Text(String(localized: "Analyzer"))
                }
                .font(.defaultFontCaption)
            
            // NEW FEATURES 0.2
            MultiSelectView()
                .tag(2)
                .tabItem {
                    Image(systemName: "chart.bar.doc.horizontal")
                        .renderingMode(.template)
                    Text(String(localized: "Multi-select"))
                }
            
            MasterPaletteListView()
                .tag(3)
                .tabItem {
                    Image(systemName: "figure.dance")
                        .renderingMode(.template)
                    Text(String(localized: "Masters"))
                }
//            CreatePaletteWithPhotosView()
//                .tag(4)
//                .tabItem {
//                    Image(systemName: "chart.bar.doc.horizontal")
//                        .renderingMode(.template)
//                    Text(String(localized: "Multi-select"))
//                }
        }
        .tint(.indigo)
    }
}

#Preview {
    ReginaldKuenstlerTabView()
}
