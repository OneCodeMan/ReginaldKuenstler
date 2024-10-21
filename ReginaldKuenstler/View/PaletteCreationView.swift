//
//  PaletteCreationView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct PaletteColourSelectItem: Identifiable {
    let id = UUID()
    var paletteColour: PaletteColour
    var isSelected: Bool
}

struct PaletteCreationView: View {
    @ObservedObject var viewModel: CreateUserPaletteViewModel = CreateUserPaletteViewModel()
    
    // MARK: Search logic
    @State private var searchText: String = ""
    
    // MARK: dismiss
    @Environment(\.dismiss) var dismiss
    
    // Grid layout with 3 columns
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    var body: some View {
        NavigationStack {
            ZStack {
                VStack {
                    ScrollView {
                        // Display colours in a LazyVGrid
                        LazyVGrid(columns: columns, spacing: 16) {
                            // We need indices because of the `isSelected` logic
                            // crashes if we don't have this if statement lmfao what a joke
                            if !viewModel.filteredPaletteColourSelectItems.isEmpty {
                                ForEach(viewModel.filteredPaletteColourSelectItems.indices, id: \.self) { index in
                                    ColourGridItemView(colourItem: $viewModel.filteredPaletteColourSelectItems[index])
                                    .onTapGesture {
                                        let currentColour = viewModel.filteredPaletteColourSelectItems[index]
                                        
                                        // don't select if already owned by user
                                        if !currentColour.paletteColour.isUserOwned {
                                            viewModel.filteredPaletteColourSelectItems[index].isSelected.toggle()
                                            print("--PaletteCreationView, current colour is not owned. Toggled.")
                                        } else {
                                            print("--PaletteCreationView, current colour is already user owned. Not toggling.")
                                        }
                                       
                                        print("--PaletteCreationView, inside onTapGesture of GridItem.")
                                        print("--PaletteCreationView, selectedColour is \(viewModel.filteredPaletteColourSelectItems[index])\n")
                                    }
                                }
                            }
                            
                        }
                        .padding()
                        .scrollContentBackground(.hidden)
                        .searchable(text: $searchText)
                        .onChange(of: searchText) { search in
                            if !search.isEmpty {
                                self.viewModel.filterPaletteColours(term: search)
                            } else {
                                self.viewModel.resetFilteredPaletteColours()
                            }
                        }
                        
//                        Spacer()
                        
                    }
                    // end of scrollview
                    
                    // Button to save selected colours to UserDefaults
                    VStack(alignment: .center) {
                        Text("Selected Colours:")
                        HStack {
                            // INFO on selected colours
                            ForEach(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }) { pc in
                                Circle()
                                    .stroke(.gray, lineWidth: 2)
                                    .fill(Color(pc.paletteColour.uiColour))
                                    .frame(height: 20)
                            }
                        }
                        .padding()
                        
                        // the submit button
                        Button(action: {
                            viewModel.saveSelectedToUserDefaults()
                            self.dismiss()
                        }) {
                            Text("Save Selected Colours")
                                .padding()
                                .background(Color.blue)
                                .foregroundColor(.white)
                                .cornerRadius(8)
                        }
                        
                    }
                    .padding()
                    .frame(alignment: .bottom)
                    // end of group
                }
                .navigationTitle("Select Palette")// end of vstack
            }
           
        }
    }
}
