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
    
    // MARK: bool states
    @State private var isLoadingAfterColoursSelected: Bool = false
    
    // Grid layout with 3 columns
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    // MARK: alert states
    // when user taps on colour already owned in their palette.
    @State private var displayColourAlreadyOwnedAlert: Bool = false
    @State private var displayClearSelectionButton: Bool = false
    @State private var displayZeroSelectedColoursAlert: Bool = false
    
    var body: some View {
        NavigationStack {
            VStack {
                Text("")
                    .toolbar {
                        if !viewModel.filteredPaletteColourSelectItems.filter({ $0.isSelected }).isEmpty {
                            Button("Clear") {
                                withAnimation {
                                    viewModel.clearUserSelectedColours()
                                }
                            }
                        }
                    }
                if !isLoadingAfterColoursSelected {
                    VStack {
                        // Selection
                        List {
                            ForEach(Array(viewModel.groupedColourSelectItems.keys).sorted(), id: \.self) { groupName in
                                GroupSectionView(groupName: groupName, colourItems: viewModel.groupedColourSelectItems[groupName] ?? [], viewModel: viewModel, displayColourAlreadyOwnedAlert: $displayColourAlreadyOwnedAlert)
                            }
                        }
                        .searchable(text: $searchText)
                        .onChange(of: searchText) { search in
                            if !search.isEmpty {
                                viewModel.filterPaletteColours(term: search)
                            } else {
                                viewModel.resetFilteredPaletteColours()
                            }
                        }
                    }
                }
                
                
                // Display selected colors
                SelectedColoursView(viewModel: viewModel, isLoadingAfterColoursSelected: $isLoadingAfterColoursSelected)
                    .padding()
            }
            .navigationTitle("Create Palette")
            .onAppear {
                viewModel.fetchUserPalettes()
            }
            .alert("This colour is already in your palette.", isPresented: $displayColourAlreadyOwnedAlert) {
                
            } // alert
        }
    }
}

struct GroupSectionView: View {
    var groupName: String
    var colourItems: [PaletteColourSelectItem]
    @ObservedObject var viewModel: CreateUserPaletteViewModel  // Pass viewModel here
    @Binding var displayColourAlreadyOwnedAlert: Bool
    
    var body: some View {
        if !colourItems.isEmpty {
            VStack(alignment: .leading) {
                Text(groupName)
                    .font(.largeTitle)
                    .bold()
                    .padding([.top, .leading], 8)
                
                // Colour list
                ColourGridView(colourItems: colourItems, viewModel: viewModel, displayColourAlreadyOwnedAlert: $displayColourAlreadyOwnedAlert)  // Pass viewModel to ColourGridView
            }
            .listRowSeparator(.hidden)
        }
    }
}

struct ColourGridView: View {
    var colourItems: [PaletteColourSelectItem]
    @ObservedObject var viewModel: CreateUserPaletteViewModel
    @Binding var displayColourAlreadyOwnedAlert: Bool
    
    var body: some View {
        LazyVGrid(columns: Array(repeating: GridItem(.flexible()), count: 3)) {
            ForEach(colourItems) { cI in
                if let index = viewModel.filteredPaletteColourSelectItems.firstIndex(where: { $0.id == cI.id }) {
                    PaletteListItemView(paletteColourItem: $viewModel.filteredPaletteColourSelectItems[index])
                        .onTapGesture {
                            toggleColourSelection(for: cI)
                        }
                }
            }
            // end of foreach(colourItems)
        }
        .listRowSeparator(.hidden)
        .padding()
    }
    
    private func toggleColourSelection(for item: PaletteColourSelectItem) {
        // Update selection state
        if let index = viewModel.filteredPaletteColourSelectItems.firstIndex(where: { $0.id == item.id }) {
            if !viewModel.filteredPaletteColourSelectItems[index].paletteColour.isUserOwned {
                viewModel.filteredPaletteColourSelectItems[index].isSelected.toggle()
                print("Toggled selection for color: \(item.paletteColour.uiColour)")
            } else {
                displayColourAlreadyOwnedAlert = true
                print("user owned not toggling select")
            }
            
        }
    }
}

struct SelectedColoursView: View {
    @ObservedObject var viewModel: CreateUserPaletteViewModel
    @Binding var isLoadingAfterColoursSelected: Bool
    
    // MARK: Dismiss
    @Environment(\.dismiss) var dismiss
    
    @State private var displayNoSelectedColoursAlert: Bool = false
    @State private var displayConfirmationSelectedColoursAlert: Bool = false
    @State private var showGridLoading: Bool = false
    
    var body: some View {
        VStack(alignment: .center) {
            if isLoadingAfterColoursSelected {
                VStack {
                    if showGridLoading {
                        GridAnimationView()
                    } else {
                        VStack {
                            Spacer()
                            ProgressView() {
                                Text("Loading")
                                    .font(.title)
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
            } else {
                VStack {
                    Text("Selected Colours:")
                    HStack {
                        ForEach(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }) { pc in
                            Circle()
                                .stroke(.gray, lineWidth: 2)
                                .fill(Color(pc.paletteColour.uiColour))
                                .frame(height: 20)
                        }
                    }
                    .padding()
                    
                    Button(action: {
                        if !viewModel.filteredPaletteColourSelectItems.filter({ $0.isSelected }).isEmpty {
                            viewModel.saveSelectedToUserDefaults()
                            displayConfirmationSelectedColoursAlert = true
                        } else {
                            displayNoSelectedColoursAlert = true
                        }
                    }) {
                        Text("Save Selected Colours")
                            .padding()
                            .background(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }.isEmpty ? Color.gray : Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1)))
                            .foregroundColor(.white)
                            .cornerRadius(8)
                    }
                    // .disabled(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }.isEmpty)
                    .alert("No colours were selected.", isPresented: $displayNoSelectedColoursAlert) {
                        Button("OK", role: .cancel) {}
                    }
                    .alert("Are you sure you are finished selecting colours?", isPresented: $displayConfirmationSelectedColoursAlert) {
                        Button("YES") {
                            isLoadingAfterColoursSelected = true
                            DispatchQueue.main.asyncAfter(deadline: .now() + 4.0) {
                                dismiss()
                            }
                        }
                        Button("NO", role: .cancel) { }
                    }
                }
            }
            
        }
    }
}

